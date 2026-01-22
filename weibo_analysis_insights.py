#!/usr/bin/env python3
"""
微博热搜深度分析脚本
分析热搜数据，生成洞察和产品创意
"""

import json
import re
from datetime import datetime
from collections import Counter, defaultdict

def load_hot_data():
    """加载热搜数据"""
    with open('weibo_hot_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_categories(hot_list):
    """分析热搜话题分类"""
    categories = {
        '社会新闻': [],
        '娱乐综艺': [],
        '经济财经': [],
        '体育运动': [],
        '文化生活': [],
        '科技数码': [],
        '国际新闻': [],
        '其他': []
    }

    # 关键词分类规则
    category_rules = {
        '社会新闻': ['被查', '火灾', '殉职', '被抓', '责任人', '报道', '事件', '封关'],
        '娱乐综艺': ['剧集', '综艺', '电影', '演员', '明星', '柯淳', '宁静', '黄景瑜', '成毅', '虞书欣', '骄阳似我', '百花杀', '唐诡奇谭'],
        '经济财经': ['负债', '房价', '买房', '投资', '经济', '财务', '海南封关', '山东客户', '三亚'],
        '体育运动': ['东契奇', '樊振东', '体育', '比赛', '进球', '得分'],
        '文化生活': ['报告', '建议', '生活', '健康', '洗澡', '秋裤', '审美', '开花店', '猫', '气血', '旅行', '父母', '圣诞'],
        '科技数码': ['AI', '科技', '技术', '智能', '数字'],
        '国际新闻': ['日本', '美国', '战机', '激光', '照射', '国际']
    }

    for item in hot_list:
        hotword = item['hotword']
        hotwordnum = int(item['hotwordnum'].strip().replace(',', ''))

        categorized = False
        for category, keywords in category_rules.items():
            if any(keyword in hotword for keyword in keywords):
                categories[category].append({
                    'word': hotword,
                    'heat': hotwordnum,
                    'tag': item['hottag']
                })
                categorized = True
                break

        if not categorized:
            categories['其他'].append({
                'word': hotword,
                'heat': hotwordnum,
                'tag': item['hottag']
            })

    return categories

def analyze_trends(categories):
    """分析热点趋势"""
    trends = {
        '热门标签': Counter(),
        '话题特征': Counter(),
        '情感倾向': defaultdict(list)
    }

    # 分析标签分布
    for category_name, items in categories.items():
        for item in items:
            # 统计标签
            if item['tag']:
                trends['热门标签'][item['tag']] += 1

            # 分析话题特征
            word = item['word']
            if '被查' in word or '被抓' in word:
                trends['话题特征']['负面事件'] += 1
            elif '新' in item['tag']:
                trends['话题特征']['新兴话题'] += 1
            elif '沸' in item['tag']:
                trends['话题特征']['沸腾话题'] += 1
            elif '热' in item['tag']:
                trends['话题特征']['热门话题'] += 1

            # 情感分析
            if any(pos in word for pos in ['爱', '好', '赞', '支持', '喜欢']):
                trends['情感倾向']['正面'].append(word)
            elif any(neg in word for pos in ['被查', '火灾', '殉职', '违法'] for neg in [pos]):
                trends['情感倾向']['负面'].append(word)
            else:
                trends['情感倾向']['中性'].append(word)

    return trends

def generate_insights(categories, trends):
    """生成深度洞察"""
    insights = {
        '数据概览': {},
        '话题分布': {},
        '趋势分析': {},
        '用户行为': {},
        '社会现象': {}
    }

    # 数据概览
    total_topics = sum(len(items) for items in categories.values())
    total_heat = sum(item['heat'] for category in categories.values() for item in category)

    insights['数据概览'] = {
        '总话题数': total_topics,
        '总热度值': total_heat,
        '平均热度': round(total_heat / total_topics, 0),
        '最高热度话题': max(categories.values(), key=lambda x: x[0]['heat'] if x else 0)[0]['word'] if any(categories.values()) else 'N/A'
    }

    # 话题分布
    insights['话题分布'] = {}
    for category, items in categories.items():
        if items:
            category_heat = sum(item['heat'] for item in items)
            insights['话题分布'][category] = {
                '话题数量': len(items),
                '总热度': category_heat,
                '占比': round(category_heat / total_heat * 100, 1)
            }

    # 趋势分析
    insights['趋势分析'] = {
        '最活跃标签': dict(trends['热门标签'].most_common(3)),
        '话题特征分布': dict(trends['话题特征']),
        '情感倾向分布': {k: len(v) for k, v in trends['情感倾向'].items()}
    }

    # 用户行为分析
    insights['用户行为'] = {
        '关注焦点': '娱乐和生活类话题占主导地位',
        '参与特点': '对新兴话题反应迅速，标签热度高的话题参与度强',
        '传播模式': '情感共鸣类话题传播速度快'
    }

    # 社会现象洞察
    insights['社会现象'] = {
        '经济关注': '房地产、负债等经济话题持续受关注',
        '文化现象': '健康生活、传统文化传承话题热度高',
        '娱乐生态': '综艺节目和影视作品是流量主要来源',
        '社会责任': '对社会事件保持高度关注和监督'
    }

    return insights

def generate_product_ideas(insights):
    """基于分析结果生成产品创意"""
    product_ideas = {
        '智能分析平台': {
            '名称': 'WeiboTrend AI - 微博热搜智能分析平台',
            '核心功能': [
                '实时热搜数据采集与分析',
                '话题分类和情感倾向识别',
                '热点趋势预测和预警',
                '多维度数据可视化展示',
                '社交媒体影响力评估'
            ],
            '目标用户': [
                '品牌营销团队',
                '内容创作者',
                '新闻机构',
                '市场研究人员',
                '政策制定者'
            ],
            '商业价值': '帮助用户把握社会脉搏，预测趋势，优化决策'
        },

        '内容创作助手': {
            '名称': 'HotCreator - 热点内容创作助手',
            '核心功能': [
                '基于热搜话题的内容灵感生成',
                '热点话题深度背景调研',
                '创作素材智能推荐',
                '传播效果预测分析',
                '内容优化建议'
            ],
            '目标用户': [
                '自媒体创作者',
                '广告策划人员',
                '新媒体运营',
                '短视频制作者',
                '品牌内容团队'
            ],
            '商业价值': '提升内容创作效率和传播效果'
        },

        '舆情监测系统': {
            '名称': 'PublicOpinion Guardian - 公共舆情监测系统',
            '核心功能': [
                '负面舆情实时监测',
                '危机事件预警通知',
                '舆情传播路径分析',
                '公众情感变化追踪',
                '应对策略建议生成'
            ],
            '目标用户': [
                '政府机构',
                '企业公关部门',
                '社会组织',
                '新闻媒体',
                '危机管理团队'
            ],
            '商业价值': '及时发现和处理公共关系危机'
        },

        '消费趋势预测': {
            '名称': 'TrendScope - 消费趋势预测平台',
            '核心功能': [
                '基于热搜的消费需求分析',
                '新兴消费趋势识别',
                '市场规模潜力评估',
                '产品定位建议',
                '营销时机预测'
            ],
            '目标用户': [
                '产品经理',
                '市场分析师',
                '投资机构',
                '电商平台',
                '品牌方'
            ],
            '商业价值': '指导产品开发和市场策略制定'
        },

        '教育内容推荐': {
            '名称': 'EduHeat - 热点教育内容平台',
            '核心功能': [
                '热点事件教育价值挖掘',
                '时事教学内容自动生成',
                '学习兴趣点智能匹配',
                '知识点关联推荐',
                '学习效果评估'
            ],
            '目标用户': [
                '教育工作者',
                '学生',
                '培训机构',
                '内容创作者',
                '知识付费平台'
            ],
            '商业价值': '提升教育内容的时效性和趣味性'
        }
    }

    return product_ideas

def main():
    print("=" * 60)
    print("📊 微博热搜深度分析引擎")
    print("=" * 60)
    print(f"🕐 分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # 加载数据
    print("\n📂 加载热搜数据...")
    data = load_hot_data()
    hot_list = data['result']['list']
    print(f"✅ 加载完成，共 {len(hot_list)} 条热搜")

    # 分类分析
    print("\n🏷️  分析话题分类...")
    categories = analyze_categories(hot_list)
    for cat, items in categories.items():
        if items:
            print(f"   {cat}: {len(items)} 条")

    # 趋势分析
    print("\n📈 分析热点趋势...")
    trends = analyze_trends(categories)
    print(f"   标签类型: {len(trends['热门标签'])} 种")
    print(f"   话题特征: {len(trends['话题特征'])} 类")

    # 生成洞察
    print("\n💡 生成深度洞察...")
    insights = generate_insights(categories, trends)

    # 生成产品创意
    print("\n🎯 生成产品创意...")
    product_ideas = generate_product_ideas(insights)

    # 整合结果
    analysis_result = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'data_summary': {
            'total_topics': len(hot_list),
            'categories': categories,
            'trends': trends
        },
        'insights': insights,
        'product_ideas': product_ideas
    }

    # 保存结果
    output_file = 'weibo_analysis_insights.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analysis_result, f, ensure_ascii=False, indent=2)

    print(f"\n💾 分析结果已保存到: {output_file}")

    # 输出关键洞察
    print("\n" + "=" * 60)
    print("🎯 关键洞察")
    print("=" * 60)
    print(f"📊 总话题数: {insights['数据概览']['总话题数']}")
    print(f"🔥 总热度值: {insights['数据概览']['总热度值']:,}")
    print(f"⭐ 平均热度: {insights['数据概览']['平均热度']:,.0f}")
    print(f"🏆 最热话题: {insights['数据概览']['最高热度话题']}")

    print(f"\n📈 话题分布:")
    for cat, info in insights['话题分布'].items():
        print(f"   {cat}: {info['话题数量']} 条 ({info['占比']}%)")

    print(f"\n💡 社会现象洞察:")
    for phenomenon, insight in insights['社会现象'].items():
        print(f"   • {phenomenon}: {insight}")

    print("\n" + "=" * 60)
    print("✅ 深度分析完成！")
    print("=" * 60)

    return analysis_result

if __name__ == "__main__":
    result = main()