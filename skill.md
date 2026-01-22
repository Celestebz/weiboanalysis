# 微博热搜分析技能文档

## 核心技能说明

本技能用于分析微博热搜并生成产品创意报告，每次执行都必须包含以下关键环节：

---

## 🔍 技能1: 使用百度搜索API获取事件背景

### 功能描述
每次运行分析时，必须使用百度搜索API获取热搜事件的详细背景和来龙去脉，确保分析的深度和准确性。

### API配置
```bash
# API端点
URL: https://qianfan.baidubce.com/v2/ai_search/web_search

# 认证信息
API Key: bce-v3/ALTAK-L6TPvDXqOGEqEIB2Ogh0z/4432bd66294ce9b19fdca57204bd2024c8e40db6

# 请求头
Authorization: Bearer <API Key>
Content-Type: application/json
```

### 调用方法 (CURL)

**基础版本**（推荐）：
```bash
curl --location 'https://qianfan.baidubce.com/v2/ai_search/web_search' \
--header 'X-Appbuilder-Authorization: Bearer bce-v3/ALTAK-L6TPvDXqOGEqEIB2Ogh0z/4432bd66294ce9b19fdca57204bd2024c8e40db6' \
--header 'Content-Type: application/json' \
--data '{"messages":[{"content":"热搜话题关键词","role":"user"}]}'
```

**完整版本**（高级参数）：
```bash
curl --location 'https://qianfan.baidubce.com/v2/ai_search/chat/completions' \
--header 'Authorization: Bearer bce-v3/ALTAK-L6TPvDXqOGEqEIB2Ogh0z/4432bd66294ce9b19fdca57204bd2024c8e40db6' \
--header 'Content-Type: application/json' \
--data '{
  "messages": [
    {
      "content": "热搜话题关键词",
      "role": "user"
    }
  ]
}'
```

### Python调用方法
```python
import requests

def search_event_background(query, api_key):
    """使用百度搜索API调研事件背景信息"""
    url = "https://qianfan.baidubce.com/v2/ai_search/web_search"

    headers = {
        "X-Appbuilder-Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # 简化版本：仅使用必需参数
    data = {
        "messages": [
            {
                "content": f"详细搜索：{query}，提供事件的完整背景、时间线和影响",
                "role": "user"
            }
        ]
    }

    try:
        print(f"🔍 正在搜索: {query}")
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ 搜索失败: {e}")
        return None

# 使用示例
api_key = "bce-v3/ALTAK-L6TPvDXqOGEqEIB2Ogh0z/4432bd66294ce9b19fdca57204bd2024c8e40db6"
result = search_event_background("女孩穿光腿神器进了急诊", api_key)

# 解析结果
if result:
    references = result.get("references", [])
    for ref in references[:5]:
        print(f"标题: {ref.get('title')}")
        print(f"内容: {ref.get('content')[:100]}...")
        print(f"链接: {ref.get('url')}")
        print("-" * 50)
```

### 响应格式
```json
{
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": "AI生成的回答内容"
            }
        }
    ],
    "references": [
        {
            "id": 1,
            "url": "网页链接",
            "title": "标题",
            "date": "2025-12-19",
            "content": "内容摘要",
            "type": "web"
        }
    ],
    "request_id": "41aa80d6-19fc-420e-ab8b-57214ec7d48e",
    "usage": {
        "completion_tokens": 295,
        "prompt_tokens": 1919,
        "total_tokens": 2214
    }
}
```

### 执行标准
- ✅ 每次分析必须调用API
- ✅ 对每个热搜话题执行至少1次搜索
- ✅ 解析返回的references字段
- ✅ 提取标题、内容、日期、URL等关键信息
- ✅ 保存搜索结果到JSON文件

### ⚠️ 重要原则
**事件背景来龙去脉必须基于实际搜索结果**：
- ❌ 禁止基于推测或常识编写背景
- ❌ 禁止虚构事件细节或时间线
- ✅ 必须引用真实的搜索来源
- ✅ 背景描述要与搜索结果一致
- ✅ 如果搜索结果有限，要如实说明
- ✅ 所有背景信息必须有可追溯的来源

---

## 📊 技能2: 微博热搜数据获取

### 功能描述
获取实时微博热搜数据，作为分析的基础数据源。

### API配置
```bash
URL: https://apis.tianapi.com/weibohot/index
API Key: ab1cca5ccb089e4bed812457b6b1155a
```

### 调用方法
```bash
curl "https://apis.tianapi.com/weibohot/index?key=ab1cca5ccb089e4bed812457b6b1155a"
```

---

## 📝 技能3: 每个热搜的详细分析结构

### 必须包含的分析维度

#### 1. 背景来龙去脉 (必须基于搜索结果)
- **搜索来源**: 列出调用的搜索关键词和API响应摘要
- **事件起因**: 基于搜索结果描述的初始触发点
- **事件发展**: 基于搜索结果梳理的时间线
- **社会影响**: 基于搜索结果分析的反响
- **各方反应**: 基于搜索结果记录的各方态度

**撰写规范**：
- 每个信息点都要标注来源链接
- 引用搜索结果中的原文内容
- 如实说明搜索结果的完整性和局限性
- 禁止添加搜索结果中没有的信息

**背景撰写模板**：
```
## 背景来龙去脉

### 🔍 搜索来源
- **搜索关键词**: [具体使用的关键词]
- **API调用时间**: [时间戳]
- **返回结果数量**: [X条相关结果]

### 事件详情 (基于搜索结果)
**来源1**: [标题] - [URL]
- 摘录: "[搜索结果的原文内容]"
- 时间: [日期]

**来源2**: [标题] - [URL]
- 摘录: "[搜索结果的原文内容]"
- 时间: [日期]

### 事件时间线 (基于搜索结果)
[根据搜索结果梳理的时间线]

### 社会影响 (基于搜索结果)
[引用搜索结果中关于影响的描述]
```

**注意事项**：
- 如果搜索结果与话题相关性低，要明确说明"搜索结果相关性有限"
- 如果没有找到相关信息，要如实标注"未搜索到详细背景"
- 所有描述都要有明确的来源标注

#### 2. 深度分析
- **用户痛点**: 暴露的问题和需求
- **市场机会**: 潜在的商业价值
- **创新方向**: 技术/产品创新点

#### 3. 软件产品创意 (重点)
每个话题必须提供 **2个软件产品方案**：
- 网页应用/小程序
- 移动APP
- 在线平台/工具
- 数据可视化系统

**产品方案结构**：
- 产品名称和定位
- 核心功能描述
- 目标用户群体
- 市场潜力评估
- 技术实现方案

**避免内容**：
- ❌ 硬件产品
- ❌ 实体商品
- ❌ 纯线下服务

---

## 📄 技能4: 报告生成规范

### 命名规则
```
weibo_analysis_report_YYYYMMDD.html
```
例如：`weibo_analysis_report_251218.html`

### 报告结构
1. **数据概览** - 热搜数据统计
2. **话题深度分析** - 每个热搜的完整分析
   - 背景来龙去脉
   - 深度分析
   - 软件产品创意
3. **总结与建议** - 优先级排序和行动计划

### HTML设计要求
- 现代化响应式设计
- 清晰的信息层级
- 美观的视觉呈现
- 移动端友好

---

## ⚙️ 技能5: 任务执行流程

### 标准流程 (必须遵循)
1. **获取微博热搜数据** (必做,获取10个热搜话题)
2. **使用百度搜索API调研背景** (必做，每个话题至少1次)
3. **分析每个话题的来龙去脉** (必做)
4. **提供针对性软件产品创意** (必做，每个话题2个)
5. **生成HTML报告** (必做，使用标准命名)

### 质量标准
- 每个热搜话题必须有独立分析章节
- 每个话题必须包含背景分析和产品创意
- 所有产品方案必须是软件形态
- 报告必须可正常打开和浏览

---

## 🎯 核心原则

1. **数据驱动**: 基于真实API数据进行分析
2. **深度挖掘**: 每个话题必须有详细背景调研
3. **软件导向**: 产品创意聚焦软件解决方案
4. **实用性强**: 产品方案具备可落地性
5. **命名规范**: 严格遵循日期命名规则
6. **真实严谨**: 事件背景必须基于实际搜索结果，禁止虚构

---

## 📋 技能检查清单

执行前检查：
- [ ] 百度搜索API可正常调用
- [ ] 微博热搜API可正常获取
- [ ] 分析框架准备就绪
- [ ] 报告模板可用

执行中检查：
- [ ] 每个话题都调用了搜索API
- [ ] 每个话题都有完整的背景分析
- [ ] 每个话题都有2个软件产品创意
- [ ] 产品方案不包含硬件内容
- [ ] 背景信息全部来自搜索结果，无虚构内容
- [ ] 所有信息来源都有可追溯的链接

执行后检查：
- [ ] 报告命名符合规范
- [ ] HTML文件可正常打开
- [ ] 所有分析维度完整
- [ ] 产品创意具备可行性

---

**版本**: v1.1
**最后更新**: 2025-12-19
**维护者**: Claude Code Assistant
