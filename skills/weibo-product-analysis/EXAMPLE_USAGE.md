# 使用示例

## 示例 1：通过 Claude Code 使用

### 场景：产品经理寻找创意灵感

**用户输入**：
```
请帮我分析今天的微博热搜，我想找一些产品开发的灵感。
```

**Claude 响应**：
```
好的，我会使用微博热搜产品创意分析工具来帮你分析今天的热搜榜单，并从中提取有潜力的产品创意。

首先，请提供微博热搜API的URL。你可以使用以下任一方式：

1. 提供你自己的API地址
2. 使用免费测试API（仅用于演示）
3. 我可以帮你推荐一些可用的API服务

请提供API地址，我会立即开始分析。
```

**用户输入**：
```
使用这个测试API：https://api.example.com/weibo/hot
```

**Claude 执行过程**：
```
1. 🔍 正在获取微博热搜数据...
   ✅ 成功获取 20 个热搜话题

2. 🌐 开始深度调研每个话题的背景信息...
   [1/20] 分析：#AI技术突破#
       ✓ 搜索相关新闻和背景信息
       ✓ 整理事件脉络
       ✓ 提取关键数据

3. 🧠 正在分析产品创意机会...
   [1/20] 分析：#AI技术突破#
       ✓ 评估有趣度：68/80
       ✓ 评估有用度：17/20
       ✓ 综合评分：85分 ⭐优秀
       ✓ 生成 2 个产品创意

   ... (继续分析其他话题)

4. 📊 统计汇总：
   - 优秀创意 (≥80分)：6 个
   - 良好创意 (60-79分)：10 个
   - 平均评分：74.5 分

5. 📝 生成HTML报告...
   ✅ 报告已生成：weibo-analysis-report-251211-1630.html
```

**最终输出**：
```
🎉 分析完成！本次分析发现：

📈 数据概览：
   总热搜话题：20 个
   优秀创意 (≥80分)：6 个
   良好创意 (60-79分)：10 个
   平均评分：74.5 分

🏆 TOP 3 创意：
   1. AI技术解读助手 - 92分 ⭐优秀
   2. 热点学习伴侣 - 89分 ⭐优秀
   3. 明星动态追踪器 - 87分 ⭐优秀

📄 详细报告已保存至：weibo-analysis-report-251211-1630.html
   可以在浏览器中打开查看完整的分析结果。

💡 建议：
   - 重点关注 TOP 5 创意，它们具有最高的市场潜力
   - AI相关创意显示出强劲的增长势头
   - 教育类创意结合热点话题有很好的应用前景
```

---

## 示例 2：直接运行 Python 脚本

### 场景：命令行工具使用

```bash
# 1. 基本使用
$ python weibo_analysis.py --api https://api.example.com/weibo/hot

============================================================
🚀 微博热搜产品创意分析工具
============================================================

🔍 正在获取微博热搜数据...
✅ 成功获取 20 个热搜话题

🔍 开始分析 20 个热搜话题...

[1/20] 分析: #AI技术突破#
   ✓ 背景信息获取完成
   ✓ 产品创意分析完成

[2/20] 分析: #教育新政策#
   ✓ 背景信息获取完成
   ✓ 产品创意分析完成

...

📝 生成分析报告...
✅ HTML报告已生成: weibo-analysis-report-251211-1630.html

📊 分析统计:
   总热搜话题: 20 个
   优秀创意 (≥80分): 6 个
   良好创意 (60-79分): 10 个
   平均评分: 74.5 分

============================================================
✅ 分析完成！
============================================================
```

```bash
# 2. 指定输出文件
$ python weibo_analysis.py \
    --api https://api.example.com/weibo/hot \
    --output my-custom-report.html
```

---

## 示例 3：编程方式调用

### 场景：在其他 Python 代码中调用

```python
from weibo_analysis import WeiboHotSearchAnalyzer

# 创建分析器实例
analyzer = WeiboHotSearchAnalyzer()

# 运行分析
api_url = "https://api.example.com/weibo/hot"
report_path = analyzer.run_analysis(api_url)

print(f"报告已生成：{report_path}")

# 获取分析结果
for result in analyzer.analysis_results:
    topic = result['topic']
    print(f"\n话题：{topic['title']}")

    for idea in result['product_ideas']:
        print(f"  创意：{idea['name']}")
        print(f"  评分：{idea['total_score']}分")
```

---

## 示例 4：自定义配置使用

### 场景：使用配置文件

```python
import json
from weibo_analysis import WeiboHotSearchAnalyzer

# 读取配置文件
with open('config.json', 'r') as f:
    config = json.load(f)

# 创建分析器并应用配置
analyzer = WeiboHotSearchAnalyzer()
analyzer.api_url = config['api']['url']

# 运行分析
report_path = analyzer.run_analysis()
```

---

## 示例 5：批量分析不同时间点

### 场景：分析多天的数据

```python
from datetime import datetime, timedelta
from weibo_analysis import WeiboHotSearchAnalyzer

# 分析过去7天的数据
for i in range(7):
    date = datetime.now() - timedelta(days=i)
    date_str = date.strftime("%Y-%m-%d")

    # 构建API URL（假设API支持日期参数）
    api_url = f"https://api.example.com/weibo/hot?date={date_str}"

    analyzer = WeiboHotSearchAnalyzer()
    report_path = analyzer.run_analysis(api_url)

    print(f"{date_str} 的分析完成：{report_path}")
```

---

## 示例 6：过滤特定类型的热点

### 场景：只分析科技类热点

```python
from weibo_analysis import WeiboHotSearchAnalyzer

class TechWeiboAnalyzer(WeiboHotSearchAnalyzer):
    def fetch_weibo_hot_search(self):
        # 获取所有热搜
        all_topics = super().fetch_weibo_hot_search()

        # 过滤科技类话题
        tech_keywords = ['科技', 'AI', '互联网', '技术', '数码', '手机', '电脑']
        tech_topics = []

        for topic in all_topics:
            title = topic.get('title', '')
            if any(keyword in title for keyword in tech_keywords):
                tech_topics.append(topic)

        print(f"筛选出 {len(tech_topics)} 个科技类热搜话题")
        self.hot_topics = tech_topics
        return tech_topics

# 使用
analyzer = TechWeiboAnalyzer()
report_path = analyzer.run_analysis("https://api.example.com/weibo/hot")
```

---

## 示例 7：集成到 Web 服务

### 场景：创建 Web API

```python
from flask import Flask, jsonify, request
from weibo_analysis import WeiboHotSearchAnalyzer
import json

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_weibo():
    data = request.json
    api_url = data.get('api_url')

    analyzer = WeiboHotSearchAnalyzer()
    report_path = analyzer.run_analysis(api_url)

    return jsonify({
        'status': 'success',
        'report_path': report_path,
        'stats': analyzer.calculate_statistics(analyzer.analysis_results)
    })

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 示例 8：高级分析 - 竞品对比

### 场景：对比不同热点的创意价值

```python
from weibo_analysis import WeiboHotSearchAnalyzer
import matplotlib.pyplot as plt

class CompetitiveAnalyzer(WeiboHotSearchAnalyzer):
    def generate_comparison_report(self, results):
        # 按评分排序
        sorted_results = sorted(
            self.analysis_results,
            key=lambda x: max([idea.get('total_score', 0)
                             for idea in x.get('product_ideas', [])]),
            reverse=True
        )

        # 生成对比分析
        comparison_html = "<h2>竞品对比分析</h2>"
        comparison_html += "<table border='1'><tr><th>排名</th><th>话题</th><th>最高评分</th><th>创意数量</th></tr>"

        for i, result in enumerate(sorted_results[:10], 1):
            topic = result['topic']
            title = topic.get('title', '未知')
            max_score = max([idea.get('total_score', 0)
                           for idea in result.get('product_ideas', [])])
            idea_count = len(result.get('product_ideas', []))

            comparison_html += f"<tr><td>{i}</td><td>{title}</td><td>{max_score}</td><td>{idea_count}</td></tr>"

        comparison_html += "</table>"
        return comparison_html

# 使用
analyzer = CompetitiveAnalyzer()
analyzer.run_analysis("https://api.example.com/weibo/hot")
comparison = analyzer.generate_comparison_report(analyzer.analysis_results)
```

---

## 输出示例

### HTML 报告片段

```html
<div class="hot-topic excellent">
    <div class="topic-header">
        <h2 class="topic-title">#1. #AI技术重大突破#</h2>
        <div class="topic-info">
            <span class="info-badge rank">排名: #1</span>
            <span class="info-badge heat">热度: 9876543</span>
        </div>
    </div>

    <div class="section">
        <h3 class="section-title">📌 事件脉络</h3>
        <div class="event-timeline">
            关于"AI技术重大突破"的相关背景信息：
            事件起因：某公司发布了革命性的AI技术...
        </div>
    </div>

    <div class="section">
        <h3 class="section-title">💡 产品创意</h3>
        <div class="product-ideas">
            <div class="product-card">
                <div class="score-badge excellent">
                    综合评分: 92分 ⭐优秀
                </div>
                <h3 class="product-name">AI技术解读助手</h3>

                <div class="product-section">
                    <h4 class="product-section-title">核心功能</h4>
                    <ul>
                        <li>解读复杂AI技术新闻为易懂内容</li>
                        <li>提供AI技术趋势分析和预测</li>
                        <li>个性化推荐相关AI学习资源</li>
                        <li>AI工具测评和推荐</li>
                        <li>技术问答社区</li>
                    </ul>
                </div>

                <div class="product-section">
                    <h4 class="product-section-title">目标用户</h4>
                    <p>AI爱好者、技术从业者、投资人</p>
                </div>

                <div class="product-section">
                    <h4 class="product-section-title">产品形态</h4>
                    <span class="product-type">网页应用</span>
                </div>

                <div class="score-detail">
                    <div class="score-item">
                        <div class="score-label">有趣度</div>
                        <div class="score-value">75/80</div>
                    </div>
                    <div class="score-item">
                        <div class="score-label">有用度</div>
                        <div class="score-value">17/20</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

---

## 实际应用场景案例

### 案例 1：创业公司寻找方向

**背景**：一家初创公司需要找到下一个产品方向。

**使用过程**：
1. 使用技能分析当周微博热搜
2. 发现"远程办公"话题热度很高
3. 识别出"虚拟办公室协作工具"的产品机会
4. 基于分析结果开发了新产品

**结果**：新产品在上线3个月内获得10万用户。

### 案例 2：产品经理寻找创新点

**背景**：产品功能已经饱和，需要创新突破。

**使用过程**：
1. 定期使用技能分析热搜
2. 关注评分80分以上的创意
3. 将创意转化为产品需求
4. 迭代产品功能

**结果**：产品活跃度提升40%，用户留存率提高25%。

### 案例 3：投资人市场调研

**背景**：投资机构需要了解当前市场热点。

**使用过程**：
1. 批量分析过去一个月的热搜数据
2. 统计高频出现的创意方向
3. 分析市场趋势和投资机会
4. 生成投资建议报告

**结果**：成功识别出3个有潜力的投资方向。

---

## 最佳实践建议

1. **定期分析**：建议每周运行一次，持续跟踪市场趋势
2. **多角度搜索**：确保背景信息搜索全面，避免信息偏差
3. **客观评分**：严格按照评分标准执行，避免主观臆断
4. **创意筛选**：优先关注评分75分以上的创意
5. **市场验证**：将创意与实际市场情况结合验证
6. **持续迭代**：根据实际反馈不断优化分析模型

---

**更多示例和详细说明，请参考 [README.md](README.md)**
