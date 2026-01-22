# 📚 项目文档索引

## 🎯 新手快速导航

| 需求 | 推荐文档 | 预计阅读时间 |
|------|----------|-------------|
| 第一次使用 | [START_HERE.md](START_HERE.md) | 5分钟 |
| 只想快速试试 | [快速开始.bat](快速开始.bat) 或 [快速开始.sh](快速开始.sh) | 1分钟 |
| 查看功能说明 | [README.md](README.md) | 15分钟 |
| 了解API使用 | [API_USAGE_GUIDE.md](API_USAGE_GUIDE.md) | 10分钟 |
| 学习使用示例 | [EXAMPLE_USAGE.md](EXAMPLE_USAGE.md) | 20分钟 |

## 📖 文档分类

### 🚀 入门指南
- **[START_HERE.md](START_HERE.md)** - 30秒快速开始指南
- **[快速开始.bat](快速开始.bat)** - Windows一键启动
- **[快速开始.sh](快速开始.sh)** - Mac/Linux一键启动

### 📚 详细文档
- **[README.md](README.md)** - 完整使用说明和最佳实践
- **[API_USAGE_GUIDE.md](API_USAGE_GUIDE.md)** - 天API详细使用指南
- **[EXAMPLE_USAGE.md](EXAMPLE_USAGE.md)** - 8种使用场景示例

### 🔧 技术文档
- **[SKILL.md](SKILL.md)** - Claude Code技能定义规范
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - 项目总结和技术特点
- **[weibo_analysis.py](weibo_analysis.py)** - 主程序源代码

### 🧪 测试与演示
- **[test_with_real_api.py](test_with_real_api.py)** - 真实API测试脚本
- **[test_example.py](test_example.py)** - 模拟数据演示脚本
- **[report-template.html](report-template.html)** - HTML报告模板

### ⚙️ 配置与设置
- **[config.json](config.json)** - 配置文件
- **[requirements.txt](requirements.txt)** - Python依赖列表
- **[.gitignore](.gitignore)** - Git忽略文件
- **[LICENSE](LICENSE)** - MIT开源协议

## 🎬 快速体验路径

### 路径1：零基础用户（推荐）
1. 双击运行 [快速开始.bat](快速开始.bat) 或 [快速开始.sh](快速开始.sh)
2. 选择 "1. 预览API数据"
3. 选择 "3. 运行完整分析"
4. 在浏览器中打开生成的HTML报告

### 路径2：命令行用户
```bash
# 预览数据
python test_with_real_api.py preview

# 完整分析
python test_with_real_api.py full
```

### 路径3：开发者用户
```bash
# 查看源代码
cat weibo_analysis.py

# 运行测试
python test_example.py demo

# 集成到项目
from weibo_analysis import WeiboHotSearchAnalyzer
```

## 💡 按需求查找

### 我想...
- **快速试用** → [START_HERE.md](START_HERE.md)
- **了解功能** → [README.md](README.md)
- **使用真实API** → [API_USAGE_GUIDE.md](API_USAGE_GUIDE.md)
- **学习示例** → [EXAMPLE_USAGE.md](EXAMPLE_USAGE.md)
- **修改配置** → [config.json](config.json)
- **查看源码** → [weibo_analysis.py](weibo_analysis.py)
- **了解技术细节** → [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)

### 我遇到了...
- **Python环境问题** → [START_HERE.md](START_HERE.md) - 常见问题部分
- **API错误** → [API_USAGE_GUIDE.md](API_USAGE_GUIDE.md) - 故障排除部分
- **自定义需求** → [EXAMPLE_USAGE.md](EXAMPLE_USAGE.md) - 自定义示例
- **集成问题** → [README.md](README.md) - 集成指南

### 我想了解...
- **项目背景** → [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
- **技术架构** → [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - 技术特点部分
- **扩展开发** → [README.md](README.md) - 扩展开发部分
- **最佳实践** → [README.md](README.md) - 最佳实践部分

## 🔍 文件快速定位

### 文档文件
- `*.md` - 所有文档文件
- `START_HERE.md` - 快速开始（**推荐首先阅读**）
- `README.md` - 详细说明

### 代码文件
- `*.py` - Python源代码
- `weibo_analysis.py` - 主程序
- `test_with_real_api.py` - 真实API测试
- `test_example.py` - 演示脚本

### 配置文件
- `*.json` - JSON配置文件
- `config.json` - 主配置
- `requirements.txt` - 依赖

### 资源文件
- `*.html` - HTML模板
- `report-template.html` - 报告模板
- `*.bat` / `*.sh` - 启动脚本

## 📊 文件大小统计

| 文件类型 | 数量 | 总大小 |
|----------|------|--------|
| 文档 (.md) | 6个 | ~41KB |
| 代码 (.py) | 3个 | ~34KB |
| 配置 (.json/.txt) | 3个 | ~2KB |
| 模板 (.html) | 1个 | ~12KB |
| 脚本 (.bat/.sh) | 2个 | ~3KB |
| 其他 | 1个 | ~2KB |
| **总计** | **16个** | **~94KB** |

## 🎯 推荐阅读顺序

### 第一次使用
1. **[START_HERE.md](START_HERE.md)** - 快速开始（5分钟）
2. **运行快速启动脚本** - 实际体验（2分钟）
3. **[README.md](README.md)** - 详细了解（15分钟）

### 深度使用
1. **[README.md](README.md)** - 完整功能（15分钟）
2. **[API_USAGE_GUIDE.md](API_USAGE_GUIDE.md)** - API使用（10分钟）
3. **[EXAMPLE_USAGE.md](EXAMPLE_USAGE.md)** - 示例学习（20分钟）

### 开发扩展
1. **[weibo_analysis.py](weibo_analysis.py)** - 源代码阅读
2. **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - 技术架构（10分钟）
3. **[SKILL.md](SKILL.md)** - 技能规范（10分钟）

## ❓ 找不到想要的？

### 如果您需要...
- **更多示例** → 查看 [EXAMPLE_USAGE.md](EXAMPLE_USAGE.md)
- **API详情** → 查看 [API_USAGE_GUIDE.md](API_USAGE_GUIDE.md)
- **技术实现** → 查看 [weibo_analysis.py](weibo_analysis.py)
- **配置选项** → 查看 [config.json](config.json)

### 如果您想...
- **修改功能** → 编辑 `weibo_analysis.py`
- **调整参数** → 编辑 `config.json`
- **添加文档** → 创建新的 `.md` 文件
- **报告问题** → 创建 Issue

## 🌟 快速链接

### 常用操作
- [运行完整分析](test_with_real_api.py) - `python test_with_real_api.py full`
- [预览API数据](test_with_real_api.py) - `python test_with_real_api.py preview`
- [查看报告模板](report-template.html)
- [修改配置](config.json)

### 文档导航
- [快速开始](START_HERE.md)
- [详细说明](README.md)
- [使用示例](EXAMPLE_USAGE.md)
- [API指南](API_USAGE_GUIDE.md)

---

**💡 提示**：建议从 [START_HERE.md](START_HERE.md) 开始，它能帮助您快速上手！
