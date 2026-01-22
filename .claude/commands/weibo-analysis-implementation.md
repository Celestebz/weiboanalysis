# 微博热搜分析命令 - 实现详情

## 命令配置
**命令名**: `/weibo-analysis`
**文件位置**: `.claude/commands/weibo-analysis.md`

## 执行流程

### 1. 数据获取阶段
```
输入: /weibo-analysis
↓
调用: get_weibo_hot.py
↓
输出: weibo_hot_data_YYYYMMDD_HHMM.json
```

### 2. 背景调研阶段
```
热搜话题列表
↓
循环调用: baidu_search_background.py
   - 使用百度千帆API
   - API Key: bce-v3/ALTAK-L6TPvDXqOGEqEIB2Ogh0z/4432bd66294ce9b19fdca57204bd2024c8e40db6
   - 端点: https://qianfan.baidubce.com/v2/ai_search/web_search
↓
输出: baidu_search_results.json
```

### 3. 分析阶段
```
调用: weibo_analysis_insights.py
↓
处理:
   - 话题分类 (娱乐、社会、经济、体育、文化、国际)
   - 热度分析
   - 趋势预测
   - 用户行为洞察
   - 社会现象解读
↓
输出: weibo_analysis_insights.json
```

### 4. 报告生成阶段
```
调用: weibo_comprehensive_analysis_YYYYMMDD.html (生成器)
↓
输入: 所有分析结果
↓
输出: weibo_analysis_report_YYYYMMDD.html
```

## 每个热搜话题的分析结构

### 标准分析模板
```markdown
## [话题名称] - 热度: [数值]

### 📊 基本信息
- 热度值: [数字]
- 话题标签: [新/沸/热/空]
- 分类: [类别]

### 🔍 背景来龙去脉
#### 搜索来源
- **搜索关键词**: [关键词]
- **API调用时间**: [时间]
- **返回结果数量**: [X条]

#### 事件详情 (基于搜索结果)
**来源1**: [标题] - [URL]
- 摘录: "[搜索结果原文]"
- 时间: [日期]

**来源2**: [标题] - [URL]
- 摘录: "[搜索结果原文]"
- 时间: [日期]

#### 事件时间线 (基于搜索结果)
[根据搜索结果梳理]

#### 社会影响 (基于搜索结果)
[引用搜索结果]

### 💡 深度分析
**用户痛点**: [分析]
**市场机会**: [分析]
**创新方向**: [分析]

### 🎯 软件产品创意

#### 产品1: [名称]
- **类型**: 网页应用/小程序/移动APP/平台
- **核心功能**: [功能描述]
- **目标用户**: [用户群体]
- **市场价值**: [价值点]

#### 产品2: [名称]
- **类型**: 网页应用/小程序/移动APP/平台
- **核心功能**: [功能描述]
- **目标用户**: [用户群体]
- **市场价值**: [价值点]
```

## API配置详情

### 百度千帆AI搜索API
```json
{
  "url": "https://qianfan.baidubce.com/v2/ai_search/web_search",
  "headers": {
    "X-Appbuilder-Authorization": "Bearer bce-v3/ALTAK-L6TPvDXqOGEqEIB2Ogh0z/4432bd66294ce9b19fdca57204bd2024c8e40db6",
    "Content-Type": "application/json"
  },
  "request_body": {
    "messages": [
      {
        "content": "详细搜索：[热搜话题]，提供事件的完整背景、时间线和影响",
        "role": "user"
      }
    ]
  }
}
```

### 微博热搜API
```json
{
  "url": "https://apis.tianapi.com/weibohot/index",
  "params": {
    "key": "ab1cca5ccb089e4bed812457b6b1155a"
  }
}
```

## 质量标准

### 必须执行
- ✅ 每个热搜话题至少1次百度搜索API调用
- ✅ 每个话题都有完整背景分析（基于搜索结果）
- ✅ 每个话题提供2个软件产品创意
- ✅ 所有背景信息必须有来源标注
- ✅ 禁止虚构事件细节

### 输出检查
- [ ] 报告命名: `weibo_analysis_report_YYYYMMDD.html`
- [ ] HTML可正常打开
- [ ] 包含所有热搜话题的独立章节
- [ ] 产品方案全部为软件形态
- [ ] 背景信息全部来自搜索结果

## 错误处理

### API调用失败
- 记录错误日志
- 继续处理其他话题
- 在报告中标注"背景信息获取失败"

### 数据不完整
- 使用现有数据分析
- 标注数据来源和时间
- 提供分析局限性说明

### 搜索结果不足
- 如实说明"搜索结果相关性有限"
- 不添加推测内容
- 基于已知信息进行分析

---
**维护者**: Claude Code Assistant
**最后更新**: 2025-12-22