#!/usr/bin/env python3
"""
微博热搜数据获取脚本
从多个源获取最新的微博热搜数据
"""

import requests
import json
import time
from datetime import datetime
import re

def get_weibo_hot_from_weiboapi():
    """从微博API获取热搜数据"""
    try:
        print("🌐 正在从微博官方API获取热搜数据...")

        # 微博热搜API - 使用第三方接口
        url = "https://weibo.com/ajax/statuses/mymblog"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Referer': 'https://weibo.com/',
            'Connection': 'keep-alive'
        }

        # 由于微博API需要登录，这里使用备用方案
        # 尝试使用公开的热搜API
        hot_search_url = "https://weibo.com/ajax/side/hotSearch"

        response = requests.get(hot_search_url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            print("✅ 成功获取微博热搜数据")
            return data
        else:
            print(f"❌ 获取失败，状态码: {response.status_code}")
            return None

    except Exception as e:
        print(f"❌ 获取微博热搜数据出错: {e}")
        return None

def get_weibo_hot_from_backup():
    """从备用源获取微博热搜数据"""
    try:
        print("🔄 尝试从备用源获取热搜数据...")

        # 使用一个公开的热搜API
        url = "https://api.vvhan.com/api/hotlist/weiboHot"

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            print("✅ 成功从备用源获取热搜数据")
            return data
        else:
            print(f"❌ 备用源获取失败，状态码: {response.status_code}")
            return None

    except Exception as e:
        print(f"❌ 备用源获取出错: {e}")
        return None

def format_hot_data(raw_data):
    """格式化热搜数据"""
    try:
        if not raw_data:
            return None

        formatted_data = {
            "code": 200,
            "msg": "success",
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "result": {
                "list": []
            }
        }

        # 根据不同的数据源格式进行解析
        if isinstance(raw_data, dict):
            # 如果是官方API格式
            if 'data' in raw_data and 'realtime' in raw_data['data']:
                realtime_data = raw_data['data']['realtime']
                for item in realtime_data:
                    formatted_data["result"]["list"].append({
                        "hotword": item.get('word', ''),
                        "hotwordnum": f" {item.get('num', 0)}",
                        "hottag": item.get('flag', '')
                    })
            # 如果是备用API格式
            elif 'data' in raw_data and isinstance(raw_data['data'], list):
                for item in raw_data['data']:
                    formatted_data["result"]["list"].append({
                        "hotword": item.get('title', ''),
                        "hotwordnum": f" {item.get('hotNum', 0)}",
                        "hottag": item.get('tag', '')
                    })
            # 如果是vvhan API格式
            elif 'success' in raw_data and raw_data['success']:
                for i, item in enumerate(raw_data.get('data', [])):
                    formatted_data["result"]["list"].append({
                        "hotword": item.get('title', ''),
                        "hotwordnum": f" {item.get('hotNum', 0)}",
                        "hottag": ''
                    })
        return formatted_data

    except Exception as e:
        print(f"❌ 数据格式化出错: {e}")
        return None

def create_mock_hot_data():
    """创建模拟热搜数据（当API不可用时）"""
    print("📝 生成模拟热搜数据...")

    mock_hot_data = {
        "code": 200,
        "msg": "success",
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "result": {
            "list": [
                {"hotword": "2024年终总结", "hotwordnum": " 1200000", "hottag": "热"},
                {"hotword": "元旦假期安排", "hotwordnum": " 856000", "hottag": "新"},
                {"hotword": "春节档电影", "hotwordnum": " 743000", "hottag": "沸"},
                {"hotword": "AI技术发展", "hotwordnum": " 621000", "hottag": ""},
                {"hotword": "新能源汽车", "hotwordnum": " 567000", "hottag": "热"},
                {"hotword": "教育改革新政策", "hotwordnum": " 489000", "hottag": ""},
                {"hotword": "直播带货新规", "hotwordnum": " 456000", "hottag": "新"},
                {"hotword": "考研成绩查询", "hotwordnum": " 423000", "hottag": ""},
                {"hotword": "房地产市场", "hotwordnum": " 398000", "hottag": "沸"},
                {"hotword": "科技创新", "hotwordnum": " 367000", "hottag": ""},
                {"hotword": "食品安全", "hotwordnum": " 334000", "hottag": ""},
                {"hotword": "环保政策", "hotwordnum": " 312000", "hottag": ""},
                {"hotword": "互联网安全", "hotwordnum": " hottag":289000", " "热"},
                {"hotword": "健康生活", "hotwordnum": " 267000", "hottag": ""},
                {"hotword": "文化传承", "hotwordnum": " 245000", "hottag": "新"}
            ]
        }
    }

    print("✅ 模拟数据生成完成")
    return mock_hot_data

def save_hot_data(data, filename="weibo_hot_data_latest.json"):
    """保存热搜数据到文件"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"💾 数据已保存到: {filename}")
        return True
    except Exception as e:
        print(f"❌ 保存数据失败: {e}")
        return False

def main():
    print("=" * 60)
    print("📊 微博热搜数据获取工具")
    print("=" * 60)
    print(f"🕐 开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # 尝试从多个源获取数据
    hot_data = None

    # 尝试官方API
    print("\n🔍 尝试获取最新微博热搜...")
    hot_data = get_weibo_hot_from_weiboapi()

    # 如果官方API失败，尝试备用源
    if not hot_data:
        hot_data = get_weibo_hot_from_backup()

    # 如果所有API都失败，使用模拟数据
    if not hot_data:
        print("\n⚠️  所有API源都不可用，使用模拟数据")
        hot_data = create_mock_hot_data()

    # 格式化数据
    if hot_data:
        formatted_data = format_hot_data(hot_data)
        if formatted_data:
            # 保存数据
            filename = f"weibo_hot_data_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
            if save_hot_data(formatted_data, filename):
                print(f"\n📊 数据统计:")
                print(f"   总话题数: {len(formatted_data['result']['list'])}")
                print(f"   标签类型: 新、沸、热")
                print(f"   获取时间: {formatted_data['timestamp']}")

                print("\n" + "=" * 60)
                print("✅ 微博热搜数据获取完成！")
                print("=" * 60)
                return formatted_data

    print("❌ 数据获取失败")
    return None

if __name__ == "__main__":
    result = main()