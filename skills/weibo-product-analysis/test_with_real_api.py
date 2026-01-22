#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用真实API测试微博热搜分析工具
使用天API的微博热搜接口进行实际测试
"""

import json
from datetime import datetime
from weibo_analysis import WeiboHotSearchAnalyzer


def test_real_api():
    """使用真实API测试"""
    print("=" * 80)
    print("🚀 微博热搜产品创意分析工具 - 真实API测试")
    print("=" * 80)
    print()
    print("📡 使用天API微博热搜接口")
    print("🔗 API: https://apis.tianapi.com/weibohot/index")
    print()

    # 创建分析器实例
    analyzer = WeiboHotSearchAnalyzer()

    # 运行分析
    report_path = analyzer.run_analysis(
        "https://apis.tianapi.com/weibohot/index?key=ab1cca5ccb089e4bed812457b6b1155a"
    )

    if report_path:
        print()
        print("=" * 80)
        print("✅ 真实API测试完成！")
        print("=" * 80)
        print()
        print("📂 输出文件：")
        print(f"   {report_path}")
        print()
        print("🌐 可以在浏览器中打开HTML文件查看完整的分析报告")
        print()
        print("💡 下一步：")
        print("   1. 在浏览器中打开生成的HTML报告")
        print("   2. 查看每个热搜话题的产品创意分析")
        print("   3. 关注评分80分以上的优秀创意")
        print()
    else:
        print("❌ 测试失败")


def preview_api_data():
    """预览API返回的数据"""
    print("=" * 80)
    print("📡 API数据预览")
    print("=" * 80)
    print()

    analyzer = WeiboHotSearchAnalyzer()
    hot_topics = analyzer.fetch_weibo_hot_search(
        "https://apis.tianapi.com/weibohot/index?key=ab1cca5ccb089e4bed812457b6b1155a"
    )

    if hot_topics:
        print(f"✅ 成功获取 {len(hot_topics)} 个热搜话题")
        print()
        print("📋 前10个热搜话题：")
        print()

        for i, topic in enumerate(hot_topics[:10], 1):
            rank = topic.get('rank', i)
            title = topic.get('title', '未知')
            heat = topic.get('heat', 'N/A')
            tag = topic.get('tag', '')

            print(f"  {rank:2d}. {title}")
            print(f"      热度: {heat:15s}  标签: {tag}")
            print()

        # 保存原始数据到JSON文件
        output_file = "weibo-hot-search-data.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(hot_topics, f, ensure_ascii=False, indent=2)

        print(f"📄 完整数据已保存到: {output_file}")
        print()
    else:
        print("❌ 获取数据失败")


def analyze_specific_topics():
    """分析特定话题"""
    print("=" * 80)
    print("🎯 分析特定话题")
    print("=" * 80)
    print()

    analyzer = WeiboHotSearchAnalyzer()
    hot_topics = analyzer.fetch_weibo_hot_search(
        "https://apis.tianapi.com/weibohot/index?key=ab1cca5ccb089e4bed812457b6b1155a"
    )

    if not hot_topics:
        print("❌ 无法获取热搜数据")
        return

    # 只分析前5个话题
    print("🔍 分析前5个热搜话题...")
    print()

    for i, topic in enumerate(hot_topics[:5], 1):
        topic_title = topic.get('title', f'话题{i}')
        print(f"[{i}/5] 分析话题：{topic_title}")

        # 获取背景信息（模拟）
        background = analyzer.search_topic_background(topic_title)

        # 分析产品创意
        result = analyzer.analyze_product_ideas(topic, background)
        analyzer.analysis_results.append(result)

        # 显示分析结果
        for idea in result['product_ideas']:
            score = idea.get('total_score', 0)
            name = idea.get('name', '未命名产品')
            print(f"   💡 创意：{name}")
            print(f"      评分：{score}分 ({'⭐优秀' if score >= 80 else '良好' if score >= 60 else '普通'})")

        print()

    # 显示统计
    stats = analyzer.calculate_statistics(analyzer.analysis_results)
    print("📈 统计信息：")
    print(f"   分析话题数：{stats['total_topics']}")
    print(f"   优秀创意：{stats['excellent_count']} 个")
    print(f"   良好创意：{stats['good_count']} 个")
    print(f"   平均评分：{stats['average_score']} 分")
    print()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        command = sys.argv[1].lower()

        if command == "preview":
            preview_api_data()
        elif command == "analyze":
            analyze_specific_topics()
        elif command == "full":
            test_real_api()
        else:
            print(f"未知命令：{command}")
            print("可用命令：preview, analyze, full")
            print()
            print("说明：")
            print("  preview - 预览API返回的数据")
            print("  analyze - 分析前5个话题的创意")
            print("  full    - 运行完整分析并生成HTML报告")
    else:
        # 默认运行完整测试
        test_real_api()
