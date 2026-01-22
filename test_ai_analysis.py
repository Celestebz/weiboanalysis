#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试AI分析产品创意功能
"""

import json
import requests

# 百度千帆AI搜索API配置
BAIDU_API_URL = "https://qianfan.baidubce.com/v2/ai_search/web_search"
BAIDU_API_KEY = "bce-v3/ALTAK-L6TPvDXqOGEqEIB2Ogh0z/4432bd66294ce9b19fdca57204bd2024c8e40db6"

def test_analyze_topic_for_products():
    """测试AI分析功能"""

    # 加载测试数据
    with open('weibo_analysis_results_20251226_1001.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    topic = data['topics'][1]  # 怪奇物语话题
    topic_name = topic['name']
    search_result = topic['search_result']

    print(f"测试话题: {topic_name}")
    print("-" * 70)

    if not search_result or "references" not in search_result:
        print("X No search result")
        return None

    # 提取搜索结果的关键信息
    references = search_result.get("references", [])
    topic_info = ""

    for ref in references[:2]:  # 使用前2个搜索结果
        title = ref.get("title", "")
        content = ref.get("content", "")[:300]  # 限制内容长度
        if title and content:
            topic_info += f"标题: {title}\n内容: {content}\n\n"

    if not topic_info:
        print("X No valid search content")
        return None

    print("OK Got search content")
    print(f"Content length: {len(topic_info)}")

    # 构建AI分析提示
    prompt = f"""
基于以下热搜话题信息，从有趣度80分+有用度20分（总分100分）的角度，分析并生成2个软件产品创意：

热搜话题：{topic_name}
背景信息：{topic_info}

要求：
1. 第一个产品创意侧重"有趣度"（80分）- 创意新颖、有趣好玩、吸引用户
2. 第二个产品创意侧重"有用度"（20分）- 实用价值高、解决实际问题
3. 每个产品创意需要包含：
   - 产品名称（简洁有吸引力）
   - 核心功能（3-5个主要功能点）
   - 目标用户（具体描述目标用户群体）

请以JSON格式返回：
{{
    "analysis": "分析这个热搜的核心特征和用户需求",
    "products": [
        {{
            "name": "产品名称",
            "type": "微信小程序/移动APP/Web平台",
            "fun_score": 80,
            "useful_score": 20,
            "functions": ["功能1", "功能2", "功能3", "功能4", "功能5"],
            "target_users": ["用户群体1", "用户群体2", "用户群体3"],
            "value": "产品核心价值描述"
        }},
        {{
            "name": "产品名称",
            "type": "微信小程序/移动APP/Web平台",
            "fun_score": 20,
            "useful_score": 80,
            "functions": ["功能1", "功能2", "功能3", "功能4", "功能5"],
            "target_users": ["用户群体1", "用户群体2", "用户群体3"],
            "value": "产品核心价值描述"
        }}
    ]
}}
"""

    headers = {
        "X-Appbuilder-Authorization": f"Bearer {BAIDU_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "messages": [
            {
                "content": prompt,
                "role": "user"
            }
        ]
    }

    try:
        print("AI analyzing...")
        response = requests.post(BAIDU_API_URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()

        print("OK AI response")
        print(f"Response keys: {list(result.keys())}")

        # 提取AI返回的内容
        if "references" in result and result["references"]:
            ai_content = result["references"][0].get("content", "")
            print(f"AI content length: {len(ai_content)}")
            print(f"AI content first 200 chars: {ai_content[:200]}")

            # 尝试解析JSON
            try:
                start_idx = ai_content.find('{')
                end_idx = ai_content.rfind('}') + 1
                if start_idx >= 0 and end_idx > start_idx:
                    json_str = ai_content[start_idx:end_idx]
                    print(f"Extracted JSON length: {len(json_str)}")
                    parsed = json.loads(json_str)
                    print("OK JSON parsed")
                    print(f"Analysis: {parsed.get('analysis', '')[:100]}...")
                    print(f"Products count: {len(parsed.get('products', []))}")
                    return parsed
                else:
                    print("X No JSON found")
            except Exception as e:
                print(f"X JSON parse failed: {e}")
        else:
            print("X AI response no references")

        return None
    except Exception as e:
        print(f"X AI analysis failed: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    test_analyze_topic_for_products()
