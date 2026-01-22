# 🚀 微博热搜分析 - 快速启动指南

## 方法一：直接运行脚本（推荐）

### Windows用户
双击运行以下任一文件：
- `启动微博热搜分析.bat` (批处理文件)
- `启动微博热搜分析.ps1` (PowerShell脚本)

### 命令行运行
```bash
python weibo_analysis_command.py
```

---

## 方法二：在Claude中使用

### 尝试以下斜杠命令：
- `/weibo-hot` (简化版)
- `/weibo-analysis` (完整版)

> ⚠️ 如果显示"Unknown slash command"，请重启Claude Code或直接使用方法一

---

## 方法三：测试功能

### 运行测试脚本
```bash
python test_weibo_command.py
```

---

## 📋 文件说明

### 核心文件
- `weibo_analysis_command.py` - 主程序（直接运行此文件）
- `weibo_hot_data.json` - 示例热搜数据

### 启动器
- `启动微博热搜分析.bat` - Windows批处理启动器
- `启动微博热搜分析.ps1` - PowerShell启动器

### 文档
- `README_斜杠命令.md` - 详细使用说明
- `QUICKSTART.md` - 本文件（快速指南）

### 辅助脚本
- `get_weibo_hot.py` - 数据获取模块
- `baidu_search_background.py` - 背景调研模块
- `weibo_analysis_insights.py` - 深度分析模块

---

## 🔧 环境要求

### 必需
- Python 3.x
- 网络连接
- 依赖库：requests

### 安装依赖
```bash
pip install requests
```

---

## 📊 输出文件

执行成功后会在当前目录生成：

1. `weibo_analysis_report_YYYYMMDD.html` - HTML可视化报告
2. `weibo_analysis_results_YYYYMMDD_HHMM.json` - JSON数据文件
3. `weibo_hot_data_YYYYMMDD_HHMM.json` - 原始热搜数据

---

## 🆘 故障排除

### 问题1：Python未找到
**解决方案**：安装Python 3.x并添加到PATH环境变量

### 问题2：网络错误
**解决方案**：检查网络连接，确保可以访问外部API

### 问题3：模块导入错误
**解决方案**：
```bash
pip install requests
```

### 问题4：斜杠命令不识别
**解决方案**：
1. 重启Claude Code
2. 使用方法一直接运行脚本
3. 尝试简化命令：`/weibo-hot`

---

## 📞 技术支持

### API配置
- 百度AI搜索API（已内置）
- 微博热搜API（已内置）

### 配置文件
- API密钥已硬编码在脚本中
- 无需额外配置

### 错误日志
程序运行时会显示详细进度和错误信息

---

## 💡 使用提示

1. **首次运行**：建议先运行测试脚本
2. **网络稳定**：确保网络连接稳定
3. **耐心等待**：完整分析约需30-60秒
4. **查看报告**：重点查看HTML报告的完整内容
5. **数据安全**：所有数据仅保存在本地

---

## 🎯 核心功能

✅ 自动获取微博热搜数据
✅ 使用百度AI搜索深度调研背景
✅ 智能话题分类（娱乐、社会、经济等）
✅ 每个话题生成2个软件产品创意
✅ 输出HTML可视化报告
✅ JSON格式的结构化数据

---

**🚀 现在就开始使用吧！**