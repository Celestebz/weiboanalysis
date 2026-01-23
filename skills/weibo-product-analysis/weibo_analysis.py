#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微博热搜产品创意分析工具
基于Claude Code Skills的自动分析脚本

功能：
1. 获取微博热搜榜单数据
2. 搜索每个热点的背景信息 (使用 DuckDuckGo)
3. AI分析产品创意 (使用 Anthropic API)
4. 生成HTML分析报告

作者: Claude Code
版本: 2.0.0 (GitHub Actions Ready)
"""

import json
import os
import time
from datetime import datetime
from typing import List, Dict, Any
import requests
from pathlib import Path

# 尝试导入高级依赖
try:
    from anthropic import Anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

try:
    from duckduckgo_search import DDGS
    HAS_DDGS = True
except ImportError:
    HAS_DDGS = False

class WeiboHotSearchAnalyzer:
    """微博热搜产品创意分析器"""

    def __init__(self, api_url: str = None):
        """
        初始化分析器

        Args:
            api_url: 微博热搜API的URL
        """
        # 优先使用环境变量中的配置
        self.api_url = api_url or os.environ.get("WEIBO_API_URL")
        self.anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY")
        # 支持自定义 Base URL，默认为云雾 AI
        self.anthropic_base_url = os.environ.get("ANTHROPIC_BASE_URL", "https://yunwu.ai")
        # 百度搜索配置
        self.baidu_api_key = os.environ.get("BAIDU_API_KEY")
        
        self.hot_topics = []
        self.analysis_results = []
        
        if not HAS_ANTHROPIC:
            raise ImportError("❌ 未安装 anthropic 库，无法进行真实分析。请安装: pip install anthropic")
        
        if not self.anthropic_api_key:
            raise ValueError("❌ 未配置 ANTHROPIC_API_KEY 环境变量，无法进行真实分析。")

        # 初始化 Anthropic 客户端，指向第三方 API
        self.client = Anthropic(
            api_key=self.anthropic_api_key,
            base_url=self.anthropic_base_url
        )
        print(f"✅ Anthropic API 客户端已初始化 (Base URL: {self.anthropic_base_url})")
        if self.baidu_api_key:
            print("✅ 百度智能搜索 API 已配置")

    def fetch_weibo_hot_search(self) -> List[Dict[str, Any]]:
        """获取微博热搜榜单"""
        print("🔍 正在获取微博热搜数据...")

        if not self.api_url:
            print("❌ 请提供微博热搜API URL (通过参数或 WEIBO_API_URL 环境变量)")
            return []

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Referer": "https://s.weibo.com/"
            }
            response = requests.get(self.api_url, headers=headers, timeout=15)
            response.raise_for_status()
            data = response.json()

            self.hot_topics = []

            # 几种常见的API格式适配
            items = []
            if isinstance(data, dict):
                if 'data' in data:
                    if isinstance(data['data'], list):
                        items = data['data']
                    # 适配微博官方接口 data.data.realtime 或 data.realtime
                    elif isinstance(data['data'], dict) and 'realtime' in data['data']:
                        items = data['data']['realtime']
                elif 'result' in data and isinstance(data['result'], dict) and 'list' in data['result']:
                    items = data['result']['list']
                elif 'list' in data and isinstance(data['list'], list):
                    items = data['list']
            elif isinstance(data, list):
                items = data

            if not items:
                print(f"⚠️ 未能解析出热搜列表，原始响应: {str(data)[:200]}")
                return []

            for i, item in enumerate(items[:15]): # 取前15个
                # 适配字段 - 恢复对 TianAPI (hotword) 和其他格式的支持
                title = item.get('word') or item.get('keyword') or item.get('title') or item.get('hotword') or item.get('note')
                heat = item.get('num') or item.get('hot_word_num') or item.get('heat') or item.get('hotwordnum') or 'N/A'
                rank = i + 1
                
                if title:
                    self.hot_topics.append({
                        "rank": rank,
                        "title": title,
                        "heat": heat
                    })
                elif i == 0:
                    # 如果第一条就没有标题，打印一下它的键值，方便调试
                    print(f"⚠️ 第一条数据未找到标题字段，可用键: {list(item.keys())}")
            
            print(f"✅ 成功获取 {len(self.hot_topics)} 个热搜话题")
            return self.hot_topics

        except Exception as e:
            print(f"❌ 获取热搜失败: {e}")
            raise

    def search_topic_background_baidu(self, topic_title: str, api_key: str) -> str:
        """使用百度智能搜索API获取背景"""
        url = "https://qianfan.baidubce.com/v2/ai_search/web_search"
        headers = {
            "X-Appbuilder-Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "messages": [
                {
                    "content": f"详细搜索：{topic_title}，简述事件背景、来龙去脉",
                    "role": "user"
                }
            ]
        }
        
        try:
            response = requests.post(url, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            result_json = response.json()
            
            # 优先使用 AI 生成的总结，如果没有则拼接 reference
            summary = ""
            if "choices" in result_json and len(result_json["choices"]) > 0:
                summary = result_json["choices"][0]["message"]["content"]
            
            # 如果 AI 总结很短，补充引用内容
            if len(summary) < 50 and "references" in result_json:
                refs = result_json["references"]
                ref_texts = [f"- {r.get('title')}: {r.get('content')[:100]}..." for r in refs[:3]]
                summary += "\n\n参考信息:\n" + "\n".join(ref_texts)
                
            if summary:
                print(f"   ✅ [Baidu] 成功获取背景 ({len(summary)} 字符)")
                return summary
            else:
                print("   ⚠️ [Baidu] 返回结果为空")
                return ""
                
        except Exception as e:
            print(f"   ⚠️ [Baidu] 搜索出错: {e}")
            return ""

    def search_topic_background(self, topic_title: str) -> str:
        """搜索话题背景信息 (优先百度，降级为 DuckDuckGo)"""
        print(f"   Searching background for: {topic_title}...")
        
        # 1. 优先尝试百度搜索 API (如果配置了KEY)
        if self.baidu_api_key:
            res = self.search_topic_background_baidu(topic_title, self.baidu_api_key)
            if res:
                return res
            else:
                print("   ⚠️ 百度搜索失败，尝试切换到备用搜索...")

        # 2. 备用: DuckDuckGo 搜索
        if not HAS_DDGS:
            print(f"   ⚠️ 警告: 缺少 duckduckgo-search 库，跳过背景搜索")
            return "无法获取背景信息(缺少依赖)"
            
        try:
            with DDGS() as ddgs:
                results = []
                # 尝试策略 1: 加上"事件详情"后缀
                try:
                    query1 = f"{topic_title} 事件详情"
                    results = list(ddgs.text(query1, max_results=3))
                except Exception as e:
                    print(f"   ⚠️ 策略1搜索出错 ({str(e)}), 尝试降级...")

                # 尝试策略 2: 如果没结果或出错，尝试仅搜索标题
                if not results:
                    print(f"   ⚠️ 尝试纯标题搜索: {topic_title}")
                    try:
                        results = list(ddgs.text(topic_title, max_results=3))
                    except Exception as e:
                         print(f"   ⚠️ 策略2搜索出错: {str(e)}")

                if results:
                    print(f"   ✅ [DDGS] 找到 {len(results)} 条相关信息")
                    summary = "\n".join([f"- {r['title']}: {r['body']}" for r in results])
                    return summary
                else:
                    print(f"   ❌ 所有搜索策略均未找到结果 (可能是 GitHub Actions IP 被限制)")
                    
        except Exception as e:
            print(f"   ⚠️ 搜索服务初始化失败: {e}")
            return f"暂时无法获取网络背景信息 ({str(e)})，分析将仅基于标题进行。"
        
        return "未找到相关背景信息 (网络搜索返回空)。"

    def analyze_product_ideas(self, topic: Dict[str, Any], background: str) -> Dict[str, Any]:
        """分析产品创意"""
        topic_title = topic.get('title', '未知话题')

        prompt = f"""
        作为一个资深产品经理，请分析微博热搜话题 "{topic_title}"。
        
        原始搜索背景：
        {background}
        
        任务：
        1. 首先，请基于上述原始背景信息，整理一段通顺、简洁的事件背景总结（约100字），去除无关信息。
        2. 基于该话题，构思一个"有趣度（80分）+有用度（20分）"的数字产品创意。
        
        请严格按照以下 JSON 格式返回结果（不要包含 markdown 代码块标记，只返回纯 JSON）：
        {{
            "event_summary": "经过整理润色的事件背景简述（约100字）",
            "name": "产品名称",
            "core_features": ["功能1", "功能2", "功能3", "功能4", "功能5"],
            "target_users": "目标用户群体描述",
            "product_type": "产品形态（如微信小程序、网页等）",
            "interesting_score": 75,  // 0-80分
            "usefulness_score": 15,   // 0-20分
            "total_score": 90,        // 两者之和
            "rationale": "简短的评分理由"
        }}
        """

        try:
            message = self.client.messages.create(
                model="claude-opus-4-5-20251101",
                max_tokens=1000,
                temperature=0.7,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            content = message.content[0].text
            # 初步清理Markdown标记
            cleaned_content = content.replace('```json', '').replace('```', '').strip()
            
            try:
                idea_data = json.loads(cleaned_content)
            except json.JSONDecodeError as e:
                print(f"   ⚠️ JSON解析失败: {e}")
                print(f"   ⚠️ 原始返回内容: {content[:200]}...") # 打印前200字符用于调试
                
                # 尝试更激进的提取 (提取第一个 { 和最后一个 } 之间的内容)
                try:
                    import re
                    match = re.search(r'\{.*\}', cleaned_content, re.DOTALL)
                    if match:
                        idea_data = json.loads(match.group(0))
                    else:
                        raise ValueError("无法提取有效JSON")
                except Exception:
                    # 最终兜底方案：返回一个占位结果，保证程序不崩
                    print("   ⚠️ 启用兜底数据，跳过此话题分析错误")
                    idea_data = {
                        "event_summary": background, # 解析失败时使用原始背景
                        "name": f"基于{topic_title}的创意(AI生成失败)",
                        "core_features": ["暂时无法生成功能列表", "请稍后重试"],
                        "target_users": "未知",
                        "product_type": "未知",
                        "interesting_score": 0,
                        "usefulness_score": 0,
                        "total_score": 0,
                        "rationale": "AI响应格式错误，解析失败"
                    }

            # 优先使用 AI 整理后的背景
            final_background = idea_data.get("event_summary", background)
            if not final_background:
                 final_background = background

            return {
                "topic": topic,
                "background": final_background,
                "product_ideas": [idea_data]
            }

        except Exception as e:
            print(f"   ❌ AI分析失败: {e}")
            # 不再抛出异常阻断流程，而是返回空数据
            return {
                "topic": topic,
                "background": background,
                "product_ideas": [{
                    "name": "分析出错",
                    "core_features": [],
                    "total_score": 0,
                    "target_users": "无",
                    "product_type": "无"
                }]
            }

    def calculate_statistics(self, results: List[Dict]) -> Dict[str, Any]:
        """计算统计数据"""
        total_topics = len(results)
        excellent_count = 0
        good_count = 0
        total_score = 0
        score_count = 0

        for result in results:
            for idea in result.get("product_ideas", []):
                score = idea.get("total_score", 0)
                total_score += score
                score_count += 1

                if score >= 80:
                    excellent_count += 1
                elif score >= 60:
                    good_count += 1

        average_score = round(total_score / score_count, 1) if score_count > 0 else 0

        return {
            "total_topics": total_topics,
            "excellent_count": excellent_count,
            "good_count": good_count,
            "average_score": average_score
        }

    def generate_html_report(self, output_path: str = None) -> str:
        """生成HTML报告"""
        print("📝 正在生成HTML报告...")

        # 读取HTML模板
        template_path = Path(__file__).parent / "report-template.html"
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                template = f.read()
        except FileNotFoundError:
            # 如果找不到模板，使用内置的简单模板
            template = self._get_fallback_template()

        # 计算统计数据
        stats = self.calculate_statistics(self.analysis_results)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 生成内容
        content_html = ""
        for i, result in enumerate(self.analysis_results, 1):
            topic = result["topic"]
            background = result["background"]
            product_ideas = result["product_ideas"]

            max_score = max([idea.get("total_score", 0) for idea in product_ideas]) if product_ideas else 0
            topic_class = "excellent" if max_score >= 80 else "good" if max_score >= 60 else ""

            # 话题信息
            rank = topic.get('rank', i)
            heat = topic.get('heat', 'N/A')
            title = topic.get('title', '未知话题')
            
            # 转义HTML字符
            background_html = background.replace('\n', '<br>')

            content_html += f"""
            <div class="hot-topic {topic_class}">
                <div class="topic-header">
                    <div class="topic-title">
                        <span class="rank-badge">{rank}</span>
                        {title}
                        <span class="heat-badge">🔥 {heat}</span>
                    </div>
                </div>

                <div class="topic-body">
                    <div class="topic-left">
                        <div class="section">
                            <h3 class="section-title">📌 事件背景</h3>
                            <div class="background-content">
                                {background_html}
                            </div>
                        </div>
                    </div>

                    <div class="topic-right">
                        <h3 class="section-title">💡 创意方案</h3>
                        <div class="product-ideas">
            """

            for idea in product_ideas:
                score = idea.get("total_score", 0)
                score_class = "excellent" if score >= 80 else "good"
                
                interesting = idea.get("interesting_score", 0)
                usefulness = idea.get("usefulness_score", 0)
                name = idea.get("name", "未命名产品")
                features = idea.get("core_features", [])
                target = idea.get("target_users", "未知用户")
                ptype = idea.get("product_type", "未指定")

                features_html = "".join([f"<li>{f}</li>" for f in features])

                content_html += f"""
                            <div class="product-card">
                                <div class="score-ribbon {score_class}">
                                    {score}分
                                </div>
                                <div class="product-header">
                                    <h3>{name}</h3>
                                </div>

                                <div class="product-section">
                                    <ul class="feature-list">{features_html}</ul>
                                </div>

                                <div class="meta-grid">
                                    <div class="meta-item">
                                        <div class="meta-label">目标用户</div>
                                        <div class="meta-value">{target}</div>
                                    </div>
                                    <div class="meta-item">
                                        <div class="meta-label">产品形态</div>
                                        <div class="meta-value">{ptype}</div>
                                    </div>
                                    <div class="meta-item">
                                        <div class="meta-label">有趣度</div>
                                        <div class="meta-value" style="color:var(--secondary)">{interesting}/80</div>
                                    </div>
                                    <div class="meta-item">
                                        <div class="meta-label">有用度</div>
                                        <div class="meta-value" style="color:var(--success)">{usefulness}/20</div>
                                    </div>
                                </div>
                            </div>
                """

            content_html += """
                        </div>
                    </div>
                </div>
            </div>
            """

        # 替换模板变量
        html_content = template
        replacements = {
            "{{TIMESTAMP}}": timestamp,
            "{{TOTAL_TOPICS}}": str(stats["total_topics"]),
            "{{EXCELLENT_COUNT}}": str(stats["excellent_count"]),
            "{{GOOD_COUNT}}": str(stats["good_count"]),
            "{{AVERAGE_SCORE}}": str(stats["average_score"]),
            "{{CONTENT}}": content_html,
            "{{API_SOURCE}}": self.api_url or "Env/Input"
        }
        
        for key, value in replacements.items():
            html_content = html_content.replace(key, value)

        # 确保输出目录存在
        if not output_path:
            date_id = datetime.now().strftime("%y%m%d")
            time_id = datetime.now().strftime("%H%M")
            # 默认输出到当前目录下的 reports 文件夹
            report_dir = Path("reports")
            report_dir.mkdir(exist_ok=True)
            output_path = report_dir / f"weibo-products-{date_id}-{time_id}.html"
        else:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"✅ HTML报告已生成: {output_path}")
        return str(output_path)

    def _get_fallback_template(self):
        """内置的高级HTML模板 (Backup)"""
        return """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>微博热搜产品创意分析报告</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Noto+Sans+SC:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #6366f1;
            --primary-dark: #4f46e5;
            --secondary: #8b5cf6;
            --accent: #f59e0b;
            --success: #10b981;
            --bg-gradient: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            --card-bg: rgba(255, 255, 255, 0.95);
            --text-main: #1e293b;
            --text-secondary: #64748b;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Outfit', 'Noto Sans SC', sans-serif;
            background-color: #f3f4f6;
            background-image: 
                radial-gradient(at 0% 0%, hsla(253,16%,7%,1) 0, transparent 50%), 
                radial-gradient(at 50% 0%, hsla(225,39%,30%,1) 0, transparent 50%), 
                radial-gradient(at 100% 0%, hsla(339,49%,30%,1) 0, transparent 50%);
            background-attachment: fixed;
            color: var(--text-main);
            line-height: 1.6;
            padding: 40px 20px;
            min-height: 100vh;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            margin-bottom: 50px;
            color: white;
            padding: 40px 0;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(12px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }

        .header h1 {
            font-size: 2.8rem;
            font-weight: 800;
            margin-bottom: 15px;
            text-shadow: 0 4px 6px rgba(0,0,0,0.1);
            background: linear-gradient(to right, #fff, #dadada);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .header .subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
            font-weight: 300;
            letter-spacing: 1px;
        }

        .summary {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin-bottom: 50px;
        }

        .summary-card {
            background: var(--card-bg);
            padding: 25px;
            border-radius: 16px;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid rgba(255,255,255,0.6);
        }

        .summary-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        }

        .summary-card .number {
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 5px;
        }

        .summary-card .label {
            color: var(--text-secondary);
            font-size: 0.95rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .hot-topic {
            background: var(--card-bg);
            border-radius: 20px;
            margin-bottom: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.5);
            transition: all 0.4s ease;
        }

        .hot-topic.excellent {
            border-left: 6px solid var(--accent);
        }

        .topic-header {
            padding: 30px;
            background: rgba(248, 250, 252, 0.5);
            border-bottom: 1px solid rgba(0,0,0,0.05);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 15px;
        }

        .topic-title {
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .rank-badge {
            background: var(--text-main);
            color: white;
            width: 32px;
            height: 32px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            font-size: 1rem;
            font-weight: 700;
        }

        .heat-badge {
            background: #e2e8f0;
            color: #475569;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
        }

        .topic-body {
            padding: 30px;
            display: grid;
            grid-template-columns: 1fr 1.2fr;
            gap: 40px;
        }

        @media (max-width: 900px) {
            .topic-body { grid-template-columns: 1fr; }
        }

        .section-title {
            font-size: 1.1rem;
            color: var(--text-secondary);
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 15px;
            letter-spacing: 1px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .background-content {
            background: #f8fafc;
            padding: 20px;
            border-radius: 12px;
            font-size: 0.95rem;
            color: #475569;
            line-height: 1.7;
        }

        .product-card {
            background: white;
            border-radius: 16px;
            padding: 25px;
            border: 1px solid #e2e8f0;
            position: relative;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .product-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 40px rgba(99, 102, 241, 0.15);
            border-color: var(--secondary);
            z-index: 10;
        }

        .score-ribbon {
            position: absolute;
            top: 20px;
            right: -10px;
            background: var(--primary);
            color: white;
            padding: 5px 15px;
            border-radius: 4px;
            font-weight: 700;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
            font-size: 0.9rem;
        }
        
        .score-ribbon.excellent { background: var(--accent); }
        
        .score-ribbon::after {
            content: '';
            position: absolute;
            top: 100%;
            right: 0;
            border-width: 5px;
            border-style: solid;
            border-color: #b45309 transparent transparent transparent;
        }
        .score-ribbon.excellent::after { border-top-color: #b45309; }

        .product-header h3 {
            font-size: 1.4rem;
            margin-bottom: 20px;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }

        .feature-list li {
            position: relative;
            padding-left: 24px;
            margin-bottom: 10px;
            font-size: 0.95rem;
            color: #334155;
            list-style: none;
        }

        .feature-list li::before {
            content: "✓";
            position: absolute;
            left: 0;
            color: var(--success);
            font-weight: bold;
        }

        .meta-grid {
            margin-top: 20px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            border-top: 1px solid #f1f5f9;
            padding-top: 20px;
        }

        .meta-item {
            font-size: 0.85rem;
        }

        .meta-label {
            color: var(--text-secondary);
            margin-bottom: 4px;
            font-weight: 600;
        }

        .meta-value {
            color: var(--text-main);
            font-weight: 500;
        }

        .footer {
            text-align: center;
            padding: 40px 0;
            color: rgba(255,255,255,0.7);
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>微博热搜创意洞察</h1>
            <div class="subtitle">Daily Product Insights & Analysis</div>
            <div style="margin-top: 15px; font-size: 0.9rem; opacity: 0.8;">{{TIMESTAMP}}</div>
        </div>

        <div class="summary">
            <div class="summary-card">
                <div class="number">{{TOTAL_TOPICS}}</div>
                <div class="label">Total Topics</div>
            </div>
            <div class="summary-card">
                <div class="number">{{EXCELLENT_COUNT}}</div>
                <div class="label">Top Ideas (80+)</div>
            </div>
            <div class="summary-card">
                <div class="number">{{AVERAGE_SCORE}}</div>
                <div class="label">Avg Score</div>
            </div>
        </div>

        {{CONTENT}}

        <div class="footer">
            Generated by Claude Agent • Data Source: {{API_SOURCE}}
        </div>
    </div>
</body>
</html>
        """

    def run_analysis(self, api_url: str = None) -> str:
        """运行完整分析流程"""
        print("=" * 60)
        print("🚀 微博热搜产品创意分析工具 (Cloud Edition)")
        print("=" * 60)

        if api_url:
            self.api_url = api_url

        hot_topics = self.fetch_weibo_hot_search()
        if not hot_topics:
            print("❌ 分析终止：无法获取热搜数据")
            return ""

        print(f"🔍 开始分析 {len(hot_topics)} 个热搜话题...")
        for i, topic in enumerate(hot_topics, 1):
            topic_title = topic.get('title', f'话题{i}')
            print(f"\n[{i}/{len(hot_topics)}] 分析: {topic_title}")

            background = self.search_topic_background(topic_title)
            print(f"   ✓ 背景信息获取完成")
            
            # 延时避免API速率限制
            time.sleep(2) 

            result = self.analyze_product_ideas(topic, background)
            self.analysis_results.append(result)
            print(f"   ✓ 产品创意分析完成")

        report_path = self.generate_html_report()
        print("\n✅ 全部分析流程完成！")
        return report_path


def main():
    import argparse
    parser = argparse.ArgumentParser(description="微博热搜产品创意分析工具")
    parser.add_argument("--api", type=str, help="微博热搜API的URL")
    parser.add_argument("--output", type=str, help="输出HTML报告文件路径")
    args = parser.parse_args()

    analyzer = WeiboHotSearchAnalyzer()
    analyzer.run_analysis(args.api)

if __name__ == "__main__":
    main()
