#!/usr/bin/env python3
"""
百度搜索API - 微博热搜背景调研脚本
使用百度千帆平台AI搜索功能获取热搜事件的详细背景信息
"""

import requests
import json
from datetime import datetime

def search_event_background(query, api_key):
    """使用百度搜索API调研事件背景信息"""
    url = "https://qianfan.baidubce.com/v2/ai_search/web_search"

    headers = {
        "X-Appbuilder-Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # 简化版本：仅使用必需参数
    data = {
        "messages": [
            {
                "content": f"请详细搜索并分析：{query}，提供事件的完整背景、时间线和影响",
                "role": "user"
            }
        ]
    }

    try:
        print(f"🔍 正在搜索: {query}")
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()

        result = response.json()
        return result

    except requests.exceptions.RequestException as e:
        print(f"❌ 搜索请求失败: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON解析失败: {e}")
        return None
    except Exception as e:
        print(f"❌ 未知错误: {e}")
        return None

def analyze_search_results(search_result, topic):
    """分析搜索结果，提取关键信息"""
    if not search_result:
        print(f"⚠️ 未找到 {topic} 的相关信息")
        return None

    # 检查references
    references = search_result.get("references", [])
    print(f"✅ 找到 {len(references)} 条相关信息")

    # 提取关键信息
    analysis = {
        "topic": topic,
        "total_results": len(references),
        "key_info": [],
        "sources": []
    }

    for i, ref in enumerate(references[:5], 1):  # 只分析前5个结果
        info = {
            "rank": i,
            "title": ref.get("title", "N/A"),
            "content": ref.get("content", "N/A"),
            "date": ref.get("date", "N/A"),
            "url": ref.get("url", "N/A"),
            "type": ref.get("type", "N/A")
        }
        analysis["key_info"].append(info)

        # 添加到来源列表
        analysis["sources"].append({
            "title": ref.get("title", "N/A"),
            "url": ref.get("url", "N/A")
        })

    return analysis

def main():
    # 微博热搜主要话题
    hot_topics = [
        "年度报告",
        "中戏院长郝戎被查",
        "海南封关你关心的都在这",
        "梁淞虚构了何美延的道歉信息",
        "骄阳似我",
        "零负债人群",
        "有山东客户在三亚买了上百套房",
        "发明肉色秋裤的人你赢了"
    ]

    # 百度千帆API密钥
    api_key = "bce-v3/ALTAK-L6TPvDXqOGEqEIB2Ogh0z/4432bd66294ce9b19fdca57204bd2024c8e40db6"

    print("=" * 60)
    print("📊 百度搜索API - 微博热搜背景调研")
    print("=" * 60)
    print(f"🕐 开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🎯 目标话题: {len(hot_topics)} 个")
    print("=" * 60)

    all_results = {}

    for i, topic in enumerate(hot_topics, 1):
        print(f"\n[{i}/{len(hot_topics)}] 🔎 调研话题: {topic}")
        print("-" * 60)

        # 执行搜索
        search_result = search_event_background(topic, api_key)

        if search_result:
            # 分析结果
            analysis = analyze_search_results(search_result, topic)
            if analysis:
                all_results[topic] = analysis

                # 打印前3个结果
                for info in analysis["key_info"][:3]:
                    print(f"\n📄 来源 {info['rank']}: {info['title']}")
                    print(f"📅 日期: {info['date']}")
                    print(f"📝 摘要: {info['content'][:150]}...")
                    print(f"🔗 链接: {info['url']}")
                    print("-" * 40)
        else:
            print(f"❌ 无法获取 {topic} 的背景信息")
            all_results[topic] = {"error": "搜索失败"}

        print("\n")

    # 保存结果到JSON文件
    output_file = "baidu_search_results.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)

    print("=" * 60)
    print(f"✅ 调研完成！结果已保存到: {output_file}")
    print(f"📊 成功调研话题: {len([k for k, v in all_results.items() if 'error' not in v])}/{len(hot_topics)}")
    print(f"🕐 完成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    return all_results

if __name__ == "__main__":
    results = main()
