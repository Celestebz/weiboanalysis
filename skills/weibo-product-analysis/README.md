# 微博热搜产品创意分析技能

## 概述

这是一个基于 Claude Code 的微博热搜产品创意分析技能，能够自动从微博热搜榜单中挖掘产品开发机会，为产品经理、创业者和市场分析人员提供创意灵感。

## 功能特性

### 🔥 核心功能

1. **自动抓取微博热搜** - 通过 API 获取实时热搜榜单
2. **深度背景调研** - 使用 WebSearch 工具搜索每个热点的新闻和背景信息
3. **AI 产品创意分析** - 基于有趣度（80分）+ 有用度（20分）的评分体系
4. **生成 HTML 报告** - 创建包含事件脉络、产品创意和评分的可视化报告

### 📊 评分体系

- **有趣度（80分）**：
  - 话题新颖性（20分）
  - 情感共鸣（20分）
  - 传播潜力（20分）
  - 娱乐价值（20分）

- **有用度（20分）**：
  - 实用价值（10分）
  - 市场需求（10分）

### 🎯 产品创意要素

每个产品创意包含：
- 产品名称（简洁有吸引力）
- 核心功能（3-5个主要功能点）
- 目标用户（用户画像和痛点）
- 产品形态（网页、小程序、H5等）
- 综合评分（有趣度 + 有用度）

## 文件结构

```
skills/weibo-product-analysis/
├── SKILL.md                    # 技能定义文档
├── README.md                   # 使用说明（本文件）
├── weibo_analysis.py           # Python 实现脚本
├── report-template.html        # HTML 报告模板
└── config.json                 # 配置文件（可选）
```

## 安装与使用

### 方法一：通过 Claude Code 使用（推荐）

1. **安装技能**：
   将整个 `weibo-product-analysis` 文件夹放入 Claude Code 项目的 `skills/` 目录下

2. **在对话中使用**：
   ```
   用户：请帮我分析今天的微博热搜，找出有潜力的产品创意

   Claude：好的，我会使用微博热搜产品创意分析工具来帮你。
   请提供微博热搜API的URL，或者我可以帮你查找可用的API。

   用户：使用这个API：https://api.example.com/weibo/hot

   Claude：
   1. 正在获取微博热搜数据...
   2. 发现20个热搜话题
   3. 开始深度调研每个话题的背景信息...
   4. 正在分析产品创意机会...
   5. 生成HTML报告...

   报告已生成：weibo-analysis-report-2025-12-10.html
   ```

### 方法二：直接运行 Python 脚本

1. **安装依赖**：
   ```bash
   pip install requests
   ```

2. **运行脚本**：
   ```bash
   # 指定API URL
   python weibo_analysis.py --api https://api.example.com/weibo/hot

   # 指定输出文件
   python weibo_analysis.py --api https://api.example.com/weibo/hot --output my-report.html
   ```

## API 要求

### 微博热搜 API 格式

支持的 API 返回格式示例：

**格式1：直接返回数组**
```json
[
  {
    "rank": 1,
    "title": "#话题标题#",
    "heat": "1234567"
  },
  {
    "rank": 2,
    "title": "#另一个话题#",
    "heat": "987654"
  }
]
```

**格式2：嵌套在 data 字段中**
```json
{
  "code": 200,
  "data": [
    {
      "rank": 1,
      "title": "#话题标题#",
      "heat": "1234567"
    }
  ]
}
```

### 推荐 API 服务

- **微博官方 API**：需要申请开发者权限
- **第三方聚合 API**：如 `weibo.com` 相关服务
- **免费测试 API**：用于演示和测试

## 输出报告

### HTML 报告特性

- **响应式设计**：支持桌面和移动端查看
- **评分可视化**：
  - 优秀（≥80分）：金色徽章 + 星标
  - 良好（60-79分）：蓝色徽章
  - 普通（<60分）：灰色显示
- **交互效果**：平滑滚动、悬停动画、渐入效果
- **数据统计**：总话题数、优秀创意数、良好创意数、平均评分

### 报告文件命名

```
weibo-analysis-report-{YYMMDD}-{HHMM}.html
```

例如：
- `weibo-analysis-report-251211-1630.html` (2025年12月11日 16:30)
- `weibo-analysis-report-251210-0900.html` (2025年12月10日 09:00)

## 使用场景

### 🎯 适用人群

- **产品经理**：寻找产品创新灵感
- **创业者**：发现市场机会
- **市场分析师**：跟踪热点趋势
- **内容创作者**：寻找创作主题
- **投资人**：了解市场热点

### 💼 实际应用

1. **每周热点分析** - 定期分析热搜，发现产品机会
2. **竞品分析** - 对比不同热点的创意价值
3. **市场调研** - 了解用户关注点和需求
4. **内容策略** - 为产品营销找到话题切入点
5. **投资决策** - 评估市场热度和产品潜力

## 配置选项

### 创建 config.json（可选）

```json
{
  "api": {
    "url": "https://your-api-url.com/weibo/hot",
    "timeout": 10,
    "headers": {
      "User-Agent": "YourApp/1.0"
    }
  },
  "analysis": {
    "max_topics": 20,
    "min_score_threshold": 60
  },
  "output": {
    "directory": "./reports",
    "filename_template": "weibo-analysis-report-{date}.html"
  }
}
```

## 最佳实践

### 1. API 选择
- 优先使用官方或可靠的第三方 API
- 确保 API 返回完整的热搜数据
- 注意 API 的调用频率限制

### 2. 信息搜索
- 每个热点至少搜索 2-3 次，获取多角度信息
- 优先选择权威新闻源
- 注意信息的时效性

### 3. 创意分析
- 不要局限于热点本身，要挖掘背后的需求
- 考虑产品的可持续性，不只是蹭热点
- 评分要客观，避免过度乐观

### 4. 报告生成
- 确保 HTML 格式正确，可以在浏览器中正常打开
- 使用清晰的视觉层次
- 包含生成时间和数据来源

## 常见问题

### Q: API 返回数据格式不匹配怎么办？

A: 可以在 `weibo_analysis.py` 的 `fetch_weibo_hot_search()` 方法中添加自定义解析逻辑。

### Q: 如何自定义评分标准？

A: 修改 `analyze_product_ideas()` 方法中的评分算法，或者在配置文件中添加自定义权重。

### Q: 可以分析其他平台的热搜吗？

A: 可以，只需修改 API URL 和数据解析逻辑，热搜数据的结构通常是相似的。

### Q: 如何批量分析多天的数据？

A: 可以修改脚本添加日期参数，或者创建批处理脚本来调用多次。

### Q: 报告可以导出为 PDF 吗？

A: 可以使用浏览器的"打印"功能将 HTML 报告保存为 PDF。

## 技术实现

### 核心组件

1. **WeiboHotSearchAnalyzer 类**：
   - 数据获取：`fetch_weibo_hot_search()`
   - 背景搜索：`search_topic_background()`
   - 创意分析：`analyze_product_ideas()`
   - 报告生成：`generate_html_report()`

2. **HTML 模板**：
   - 使用 `{{VARIABLE}}` 占位符
   - 支持 CSS 动画和响应式设计
   - 包含统计数据和详细分析

3. **评分算法**：
   - 有趣度：话题新颖性、情感共鸣、传播潜力、娱乐价值
   - 有用度：实用价值、市场需求

### 扩展开发

可以基于此技能开发更多功能：

- **数据持久化**：保存分析历史
- **趋势分析**：对比不同时期的热点
- **竞品对比**：分析同类产品创意
- **用户画像**：细化目标用户分析
- **市场预测**：预测热点发展趋势

## 更新日志

### v1.0.0 (2025-12-10)
- ✨ 初始版本发布
- ✅ 完整的热搜分析流程
- ✅ 评分体系和创意分析
- ✅ HTML 报告生成
- ✅ 命令行工具支持

## 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个技能！

### 开发环境设置

```bash
git clone <repository-url>
cd weibo-product-analysis
pip install -r requirements.txt
```

### 运行测试

```bash
python -m pytest tests/
```

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 联系方式

- 作者：Claude Code
- 项目地址：[GitHub Repository]
- 问题反馈：[GitHub Issues]

---

**⭐ 如果这个技能对你有帮助，请给我们一个 Star！**
