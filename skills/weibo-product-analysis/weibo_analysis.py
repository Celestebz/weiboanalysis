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
                print(f"⚠️ 未能从API响应中解析出列表数据。原始响应开头: {str(data)[:500]}")

            for i, item in enumerate(items, 1):
                # 统一字段提取
                title = item.get('title') or item.get('hotword') or item.get('word') or item.get('note') or ''
                heat = item.get('heat') or item.get('hotwordnum') or item.get('num') or '0'
                tag = item.get('tag') or item.get('hottag') or item.get('label_name') or item.get('flag') or ''
                
                if title:
                    self.hot_topics.append({
                        'rank': i,
                        'title': title.strip(),
                        'heat': str(heat).strip(),
                        'tag': tag.strip()
                    })

            # 只取前20条，避免API消耗过大
            self.hot_topics = self.hot_topics[:15]
            
            if not self.hot_topics:
                 print("❌ 解析后未发现有效话题")
                 raise ValueError("API响应解析失败，未找到有效话题")

            print(f"✅ 成功获取 {len(self.hot_topics)} 个热搜话题")
            return self.hot_topics

        except Exception as e:
            print(f"❌ 获取热搜数据失败: {e}")
            raise  # 重新抛出异常，停止执行

    def search_topic_background(self, topic_title: str) -> str:
        """搜索话题背景信息"""
        print(f"   Searching background for: {topic_title}...")
        
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
                    print(f"   ✅ 找到 {len(results)} 条相关信息")
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
        
        背景信息：
        {background}
        
        请基于"有趣度（80分）+有用度（20分）"的评分体系，构思一个相关的数字产品创意（App、小程序、H5或功能模块）。
        
        请严格按照以下 JSON 格式返回结果（不要包含 markdown 代码块标记，只返回纯 JSON）：
        {{
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
            # 清理可能的 Markdown 标记
            content = content.replace('```json', '').replace('```', '').strip()
            
            idea_data = json.loads(content)
            
            return {
                "topic": topic,
                "background": background,
                "product_ideas": [idea_data]
            }

        except Exception as e:
            print(f"   ❌ AI分析失败: {e}")
            raise RuntimeError(f"分析话题 '{topic_title}' 失败，请检查 API 调用或网络连接") from e

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
                    <h2 class="topic-title">#{rank}. {title}</h2>
                    <div class="topic-info">
                        <span class="info-badge rank">排名: #{rank}</span>
                        <span class="info-badge heat">热度: {heat}</span>
                    </div>
                </div>

                <div class="section">
                    <h3 class="section-title">📌 事件背景</h3>
                    <div class="event-timeline">
                        {background_html}
                    </div>
                </div>

                <div class="section">
                    <h3 class="section-title">💡 产品创意</h3>
                    <div class="product-ideas">
            """

            for idea in product_ideas:
                score = idea.get("total_score", 0)
                score_class = "excellent" if score >= 80 else "good" if score >= 60 else "normal"
                score_label = "⭐优秀" if score >= 80 else "良好" if score >= 60 else "普通"

                interesting = idea.get("interesting_score", 0)
                usefulness = idea.get("usefulness_score", 0)
                name = idea.get("name", "未命名产品")
                features = idea.get("core_features", [])
                target = idea.get("target_users", "未知用户")
                ptype = idea.get("product_type", "未指定")

                features_html = "".join([f"<li>{f}</li>" for f in features])

                content_html += f"""
                        <div class="product-card">
                            <div class="score-badge {score_class}">
                                综合评分: {score}分 {score_label}
                            </div>
                            <h3 class="product-name">{name}</h3>

                            <div class="product-section">
                                <h4 class="product-section-title">核心功能</h4>
                                <ul>{features_html}</ul>
                            </div>

                            <div class="product-section">
                                <h4 class="product-section-title">目标用户</h4>
                                <p>{target}</p>
                            </div>

                            <div class="product-section">
                                <h4 class="product-section-title">产品形态</h4>
                                <span class="product-type">{ptype}</span>
                            </div>

                            <div class="score-detail">
                                <div class="score-item">
                                    <div class="score-label">有趣(80)</div>
                                    <div class="score-value">{interesting}</div>
                                </div>
                                <div class="score-item">
                                    <div class="score-label">有用(20)</div>
                                    <div class="score-value">{usefulness}</div>
                                </div>
                            </div>
                        </div>
                """

            content_html += """
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
        """简单的HTML模板"""
        return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>微博热搜分析报告</title>
    <style>
        body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .hot-topic { border: 1px solid #ddd; margin-bottom: 20px; padding: 15px; border-radius: 8px; }
        .excellent { border-color: gold; border-width: 2px; }
        .score-badge { display: inline-block; padding: 5px 10px; border-radius: 4px; color: white; }
        .excellent .score-badge { background: gold; color: black; }
        .good .score-badge { background: #4299e1; }
        .product-card { background: #f9f9f9; padding: 15px; margin-top: 10px; border-radius: 6px; }
    </style>
</head>
<body>
    <h1>微博热搜产品创意分析报告</h1>
    <p>生成时间: {{TIMESTAMP}} | 话题数: {{TOTAL_TOPICS}}</p>
    <hr>
    {{CONTENT}}
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
