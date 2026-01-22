# 🚀 快速开始指南

## ⚡ 30秒快速开始

### 方式一：使用快速启动脚本（推荐）

**Windows用户**：
```bash
# 双击运行或在命令行中执行
快速开始.bat
```

**Mac/Linux用户**：
```bash
# 在终端中执行
./快速开始.sh
```

### 方式二：直接运行命令

```bash
# 安装依赖
pip install -r requirements.txt

# 预览API数据（查看热搜榜单）
python test_with_real_api.py preview

# 分析前5个话题（快速体验）
python test_with_real_api.py analyze

# 运行完整分析（生成HTML报告）
python test_with_real_api.py full
```

### 方式三：通过Claude Code使用

1. 将 `weibo-product-analysis` 文件夹放入你的 Claude Code 项目
2. 在对话中输入：
   ```
   请帮我分析微博热搜，找出产品创意
   ```
3. Claude会自动使用天API获取数据并分析

## 📁 项目文件说明

| 文件名 | 说明 |
|--------|------|
| **START_HERE.md** | 快速开始指南（本文件）|
| **README.md** | 详细使用说明 |
| **API_USAGE_GUIDE.md** | 天API使用指南 |
| **EXAMPLE_USAGE.md** | 8种使用示例 |
| **PROJECT_SUMMARY.md** | 项目总结 |
| **weibo_analysis.py** | 主程序 |
| **test_with_real_api.py** | 真实API测试脚本 |
| **test_example.py** | 模拟数据演示脚本 |
| **report-template.html** | HTML报告模板 |
| **config.json** | 配置文件 |
| **快速开始.bat** | Windows快速启动 |
| **快速开始.sh** | Mac/Linux快速启动 |

## 🎯 三种使用方式对比

| 方式 | 适用场景 | 优点 | 缺点 |
|------|----------|------|------|
| **快速启动脚本** | 新手快速体验 | 简单易用，交互式界面 | 需要手动选择 |
| **直接运行命令** | 批量处理、自动化 | 灵活，可定制 | 需要记住命令 |
| **Claude Code** | 专业用户、集成使用 | AI自动分析，智能推荐 | 需要Claude环境 |

## 📊 输出示例

### 1. 预览数据输出
```
✅ 成功获取 50 个热搜话题

📋 前10个热搜话题：

  1. 字节跳动100元餐标的免费三餐
      热度: 1093281        标签:
  2. 原来分手真的是一个人的事
      热度: 561472         标签: 热
  3. 一条vlog回顾2025
      热度: 547203         标签:
  ...
```

### 2. 分析结果输出
```
[1/5] 分析话题：字节跳动100元餐标的免费三餐
   💡 创意：员工福利追踪器
      评分：85分 ⭐优秀
   💡 创意：企业福利平台
      评分：78分 良好

[2/5] 分析话题：原来分手真的是一个人的事
   💡 创意：情感电台小程序
      评分：82分 ⭐优秀

📈 统计信息：
   分析话题数：5
   优秀创意：3 个
   良好创意：2 个
   平均评分：81.6 分
```

### 3. HTML报告

打开生成的HTML文件，您将看到：

- **美观的数据可视化**：渐变背景、卡片布局
- **评分徽章**：⭐优秀（≥80分）、良好（60-79分）
- **详细分析**：事件脉络、产品创意、目标用户
- **响应式设计**：支持手机和电脑查看

## 🔧 自定义配置

### 修改分析数量

编辑 `config.json`：
```json
{
  "analysis": {
    "max_topics": 20,  // 分析的热搜数量
    "min_score_threshold": 60  // 最低评分阈值
  }
}
```

### 修改输出目录

编辑 `config.json`：
```json
{
  "output": {
    "directory": "./reports",  // 输出目录
    "filename_template": "weibo-analysis-report-{date}.html"
  }
}
```

### 使用自己的API Key

编辑 `config.json` 或在命令行中指定：
```bash
python weibo_analysis.py \
    --api "https://apis.tianapi.com/weibohot/index?key=YOUR_API_KEY"
```

## 💡 实际应用场景

### 场景1：产品经理寻找创新点

```bash
# 每周一运行，获取最新热搜
python test_with_real_api.py full

# 查看评分80分以上的创意
# 在生成的HTML报告中筛选高分创意
```

### 场景2：创业公司市场调研

```bash
# 批量分析多天数据
for i in {0..6}; do
    python test_with_real_api.py full
    sleep 3600  # 等待1小时
done
```

### 场景3：投资人趋势分析

```bash
# 分析特定类型话题
python -c "
from test_with_real_api import FilteredAnalyzer
analyzer = FilteredAnalyzer()
analyzer.run_analysis('YOUR_API_URL')
"
```

## ❓ 常见问题

### Q: 提示"Python不是内部或外部命令"

**A**: 需要先安装Python。推荐安装Python 3.7+版本。

### Q: 提示"requests模块不存在"

**A**: 需要安装依赖包：
```bash
pip install requests
```

### Q: 提示"API返回错误"

**A**: 检查API Key是否有效，或稍后重试。

### Q: 如何查看生成的HTML报告？

**A**: 直接双击HTML文件，或在浏览器中打开。

### Q: 如何自定义评分标准？

**A**: 修改 `weibo_analysis.py` 中的 `analyze_product_ideas()` 方法。

### Q: 支持其他平台的热搜吗？

**A**: 目前支持微博热搜。如需其他平台，修改API URL和数据解析逻辑。

## 📚 更多资源

- **详细文档**：查看 `README.md`
- **API指南**：查看 `API_USAGE_GUIDE.md`
- **使用示例**：查看 `EXAMPLE_USAGE.md`
- **项目总结**：查看 `PROJECT_SUMMARY.md`

## 🎓 学习建议

1. **先预览数据**：了解热搜内容的格式
2. **再分析创意**：关注评分和创意质量
3. **查看HTML报告**：学习数据可视化方法
4. **阅读源代码**：了解技术实现细节
5. **自定义扩展**：根据需求修改代码

## 🆘 获取帮助

- **查看文档**：所有文档都在项目目录中
- **运行演示**：`python test_example.py demo`
- **测试API**：`python test_with_real_api.py preview`

## 🎉 立即开始

**最快方式**：
```bash
pip install requests
python test_with_real_api.py preview
```

**完整体验**：
```bash
pip install requests
python test_with_real_api.py full
```

---

**⭐ 祝您使用愉快！发现更多产品创意！**

---

📧 **反馈与支持**：欢迎提交 Issue 和建议
🔄 **更新日志**：关注项目更新
⭐ **给个Star**：如果对您有帮助
