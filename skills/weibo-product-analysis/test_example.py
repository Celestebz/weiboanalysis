#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微博热搜产品创意分析工具 - 测试示例
用于演示技能的工作流程（使用模拟数据）

注意：此文件使用模拟的API数据进行演示，
实际使用时需要替换为真实的微博热搜API。
"""

import json
from datetime import datetime
from weibo_analysis import WeiboHotSearchAnalyzer


# 模拟微博热搜API数据
MOCK_API_RESPONSE = [
    {
        "rank": 1,
        "title": "#AI技术重大突破#",
        "heat": "9876543"
    },
    {
        "rank": 2,
        "title": "#教育改革新政策#",
        "heat": "8765432"
    },
    {
        "rank": 3,
        "title": "#明星恋情曝光#",
        "heat": "7654321"
    },
    {
        "rank": 4,
        "title": "#新能源汽车销量#",
        "heat": "6543210"
    },
    {
        "rank": 5,
        "title": "#环保新发明#",
        "heat": "5432109"
    },
    {
        "rank": 6,
        "title": "#在线教育平台#",
        "heat": "4321098"
    },
    {
        "rank": 7,
        "title": "#游戏新技术#",
        "heat": "3210987"
    },
    {
        "rank": 8,
        "title": "#健康生活方式#",
        "heat": "2109876"
    },
    {
        "rank": 9,
        "title": "#智能家居普及#",
        "heat": "1098765"
    },
    {
        "rank": 10,
        "title": "#短视频新功能#",
        "heat": "987654"
    }
]


class MockWeiboAnalyzer(WeiboHotSearchAnalyzer):
    """使用模拟数据的分析器"""

    def fetch_weibo_hot_search(self):
        """使用模拟数据替代真实API调用"""
        print("🔍 使用模拟数据进行演示...")

        # 模拟API延迟
        import time
        time.sleep(1)

        self.hot_topics = MOCK_API_RESPONSE
        print(f"✅ 模拟数据加载完成，共 {len(self.hot_topics)} 个热搜话题")
        return self.hot_topics

    def search_topic_background(self, topic_title):
        """使用模拟的背景信息"""
        backgrounds = {
            "AI技术重大突破": """
            <strong>事件起因：</strong>某知名科技公司发布了新一代AI大模型，宣称在多个领域实现突破性进展。<br><br>
            <strong>事件发展：</strong>该消息发布后迅速在科技圈引发热议，相关话题在各大社交平台持续发酵。<br><br>
            <strong>关键节点：</strong>
            <ul>
                <li>发布会当天：技术细节公布</li>
                <li>第二天：业界专家开始评论</li>
                <li>第三天：多家公司宣布跟进</li>
            </ul>
            <strong>社会影响：</strong>引发了公众对AI技术发展的广泛关注，同时也引发了对AI安全的讨论。<br><br>
            <strong>相关数据：</strong>话题阅读量超过10亿，讨论量超过500万条。
            """,
            "教育改革新政策": """
            <strong>事件起因：</strong>教育部发布了新的教育改革政策，涉及考试制度、课程设置等多个方面。<br><br>
            <strong>事件>政策发布后发展：</strong，家长、学生、教师群体反应强烈，<br><br>
意见分歧较大。            <strong>关键节点：</strong>
            <ul>
                <li>政策发布当天：官方解读</li>
                <li>一周后：地方实施细则出台</li>
                <li>一个月后：试点地区开始执行</li>
            </ul>
            <strong>社会影响：</strong>改变了教育资源分配方式，对学生升学路径产生重大影响。<br><br>
            <strong>相关数据：</strong>涉及全国2亿学生家庭，政策影响范围广泛。
            """,
            "明星恋情曝光": """
            <strong>事件起因：</strong>某知名明星的恋情被媒体曝光，引发粉丝和公众关注。<br><br>
            <strong>事件发展：</strong>事件在社交媒体上快速传播，话题持续占据热搜榜首位。<br><br>
            <strong>关键节点：</strong>
            <ul>
                <li>爆料当天：热搜爆了</li>
                <li>第二天：双方回应</li>
                <li>第三天：粉丝反应分化</li>
            </ul>
            <strong>社会影响：</strong>引发了对明星隐私、粉丝文化等话题的讨论。<br><br>
            <strong>相关数据：</strong>话题热度超过1亿，参与讨论的网友超过1000万。
            """,
            "新能源汽车销量": """
            <strong>事件起因：</strong>某新能源车企公布季度销量数据，同比增长超过200%。<br><br>
            <strong>事件发展：</strong>数据发布后引发行业震动，投资者和消费者高度关注。<br><br>
            <strong>关键节点：</strong>
            <ul>
                <li>财报发布：销量数据公布</li>
                <li>分析师会议：详细解读</li>
                <li>行业对比：市场份额分析</li>
            </ul>
            <strong>社会影响：</strong>推动了新能源汽车行业的整体发展，加速了燃油车退出市场的进程。<br><br>
            <strong>相关数据：</strong>新能源汽车市场渗透率达到35%，创历史新高。
            """,
            "环保新发明": """
            <strong>事件起因：</strong>某研究团队开发出新型环保材料，可完全降解且成本低廉。<br><br>
            <strong>事件发展：</strong>发明一经公布即引起环保组织和企业的广泛关注。<br><br>
            <strong>关键节点：</strong>
            <ul>
                <li>论文发表：研究成果公开</li>
                <li>媒体报道：引起关注</li>
                <li>企业接洽：商业化洽谈</li>
            </ul>
            <strong>社会影响：</strong>为解决塑料污染问题提供了新思路，有望改变整个包装行业。<br><br>
            <strong>相关数据：</strong>该材料成本比传统材料低30%，降解时间缩短至30天。
            """
        }

        # 返回匹配的背景或默认背景
        for key, bg in backgrounds.items():
            if key in topic_title:
                return bg

        return f"""
        <strong>事件起因：</strong>{topic_title}引发了广泛关注和讨论。<br><br>
        <strong>事件发展：</strong>该话题在社交媒体上快速传播，引发了网友的热议。<br><br>
        <strong>关键节点：</strong>多个关键时间点推动了该话题的持续发酵。<br><br>
        <strong>社会影响：</strong>该话题反映了当前社会的关注焦点和公众情绪。<br><br>
        <strong>相关数据：</strong>涉及人数众多，影响范围广泛。
        """


def run_demo():
    """运行演示"""
    print("=" * 80)
    print("🎉 微博热搜产品创意分析工具 - 演示模式")
    print("=" * 80)
    print()
    print("📌 说明：此演示使用模拟数据展示技能功能")
    print("🔗 实际使用时，需要提供真实的微博热搜API URL")
    print()

    # 创建分析器（使用模拟数据）
    analyzer = MockWeiboAnalyzer()

    # 运行分析
    report_path = analyzer.run_analysis()

    if report_path:
        print()
        print("=" * 80)
        print("✅ 演示完成！")
        print("=" * 80)
        print()
        print("📂 输出文件：")
        print(f"   {report_path}")
        print()
        print("🌐 可以在浏览器中打开HTML文件查看完整的分析报告")
        print()
        print("💡 实际使用提示：")
        print("   1. 提供真实的微博热搜API URL")
        print("   2. 工具会自动搜索每个热点的背景信息")
        print("   3. AI会分析产品创意机会")
        print("   4. 生成专业的HTML分析报告")
        print()
    else:
        print("❌ 演示失败")


def show_sample_analysis():
    """展示分析结果示例"""
    print("\n" + "=" * 80)
    print("📊 分析结果示例")
    print("=" * 80)
    print()

    # 创建分析器
    analyzer = MockWeiboAnalyzer()
    analyzer.fetch_weibo_hot_search()

    print("🔍 开始分析前3个话题...")
    print()

    # 只分析前3个话题作为示例
    for i, topic in enumerate(analyzer.hot_topics[:3], 1):
        topic_title = topic.get('title', '未知话题')
        print(f"[{i}/3] 分析话题：{topic_title}")

        # 获取背景信息
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


def export_json_report():
    """导出JSON格式的分析报告"""
    print("\n" + "=" * 80)
    print("📄 导出JSON格式报告")
    print("=" * 80)
    print()

    analyzer = MockWeiboAnalyzer()
    analyzer.fetch_weibo_hot_search()

    # 分析所有话题
    for topic in analyzer.hot_topics:
        topic_title = topic.get('title', '未知话题')
        background = analyzer.search_topic_background(topic_title)
        result = analyzer.analyze_product_ideas(topic, background)
        analyzer.analysis_results.append(result)

    # 导出为JSON
    export_data = {
        "timestamp": datetime.now().isoformat(),
        "total_topics": len(analyzer.hot_topics),
        "analysis_results": analyzer.analysis_results,
        "statistics": analyzer.calculate_statistics(analyzer.analysis_results)
    }

    output_file = "weibo-analysis-demo.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, ensure_ascii=False, indent=2)

    print(f"✅ JSON报告已导出：{output_file}")
    print()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        command = sys.argv[1].lower()

        if command == "demo":
            run_demo()
        elif command == "sample":
            show_sample_analysis()
        elif command == "export":
            export_json_report()
        else:
            print(f"未知命令：{command}")
            print("可用命令：demo, sample, export")
    else:
        # 默认运行完整演示
        run_demo()
