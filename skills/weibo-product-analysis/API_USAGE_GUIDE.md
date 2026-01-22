# 天API使用指南

## 📡 API信息

**接口名称**：微博热搜榜
**API地址**：https://apis.tianapi.com/weibohot/index
**API Key**：ab1cca5ccb089e4bed812457b6b1155a
**返回格式**：JSON
**数据来源**：天API

## 🔑 API认证

天API使用API Key进行认证。您有两种方式提供API Key：

### 方式一：在URL中直接提供（推荐）
```
https://apis.tianapi.com/weibohot/index?key=YOUR_API_KEY
```

### 方式二：在请求头中提供
```
headers = {
    "X-API-Key": "YOUR_API_KEY"
}
```

## 📊 返回数据格式

### 成功响应（code: 200）
```json
{
  "code": 200,
  "msg": "success",
  "result": {
    "list": [
      {
        "hotword": "字节跳动100元餐标的免费三餐",
        "hotwordnum": " 1093281",
        "hottag": "\n                                                                \n                                    \n                                \n                                                            "
      },
      {
        "hotword": "原来分手真的是一个人的事",
        "hotwordnum": "剧集 561472",
        "hottag": "热"
      }
    ]
  }
}
```

### 字段说明
- **hotword**：热搜词/话题标题
- **hotwordnum**：热度数值（可能包含前缀，如"剧集"、"综艺"等）
- **hottag**：标签（"热"、"沸"、"新"、"官宣"等）

### 错误响应示例
```json
{
  "code": 400,
  "msg": "错误的请求参数"
}
```

## 🚀 快速开始

### 方法一：使用Python脚本（推荐）

```bash
# 进入项目目录
cd skills/weibo-product-analysis

# 安装依赖
pip install -r requirements.txt

# 使用真实API运行完整分析
python test_with_real_api.py full

# 只预览API数据
python test_with_real_api.py preview

# 分析前5个话题
python test_with_real_api.py analyze
```

### 方法二：使用主程序

```bash
# 运行完整分析
python weibo_analysis.py --api "https://apis.tianapi.com/weibohot/index?key=ab1cca5ccb089e4bed812457b6b1155a"

# 指定输出文件
python weibo_analysis.py \
    --api "https://apis.tianapi.com/weibohot/index?key=ab1cca5ccb089e4bed812457b6b1155a" \
    --output my-report.html
```

### 方法三：在Python代码中调用

```python
from weibo_analysis import WeiboHotSearchAnalyzer

# 创建分析器
analyzer = WeiboHotSearchAnalyzer()

# 使用天API
api_url = "https://apis.tianapi.com/weibohot/index?key=ab1cca5ccb089e4bed812457b6b1155a"

# 运行分析
report_path = analyzer.run_analysis(api_url)

print(f"报告已生成：{report_path}")
```

## 📡 API测试

### 使用curl测试

```bash
# 获取微博热搜数据
curl -s "https://apis.tianapi.com/weibohot/index?key=ab1cca5ccb089e4bed812457b6b1155a" | jq

# 格式化输出
curl -s "https://apis.tianapi.com/weibohot/index?key=ab1cca5ccb089e4bed812457b6b1155a" | python -m json.tool
```

### 使用Postman测试

1. 创建新的GET请求
2. URL输入：`https://apis.tianapi.com/weibohot/index?key=ab1cca5ccb089e4bed812457b6b1155a`
3. 发送请求
4. 查看响应数据

### 在浏览器中测试

直接在浏览器中打开：
```
https://apis.tianapi.com/weibohot/index?key=ab1cca5ccb089e4bed812457b6b1155a
```

## 🔧 数据处理

### 自动适配

我们的工具会自动适配天API的数据格式，将：
- `hotword` → `title`（热搜标题）
- `hotwordnum` → `heat`（热度值）
- `hottag` → `tag`（标签）
- 列表索引 → `rank`（排名）

### 数据清洗

工具会自动处理：
- 去除空格和换行符
- 解析热度数值
- 提取标签信息

### 示例输出

经过处理后的数据结构：
```python
[
  {
    "rank": 1,
    "title": "字节跳动100元餐标的免费三餐",
    "heat": "1093281",
    "tag": ""
  },
  {
    "rank": 2,
    "title": "原来分手真的是一个人的事",
    "heat": "561472",
    "tag": "热"
  }
]
```

## ⚠️ 注意事项

### API限制

- **请求频率**：天API有调用频率限制，请勿频繁请求
- **数据缓存**：建议缓存热搜数据，避免重复请求
- **错误处理**：请处理API调用失败的情况

### 数据准确性

- 热搜数据实时更新，不同时间获取的数据可能不同
- 热度数值可能有前缀（如"剧集"、"综艺"等）
- 标签信息可能为空或包含特殊字符

### 使用建议

1. **定期更新**：建议每2-4小时更新一次数据
2. **并发控制**：避免同时发起多个API请求
3. **错误重试**：实现指数退避的重试机制
4. **数据验证**：检查数据完整性和有效性

## 📈 实际应用示例

### 示例1：每日热搜分析

```python
from datetime import datetime
from weibo_analysis import WeiboHotSearchAnalyzer

# 创建分析器
analyzer = WeiboHotSearchAnalyzer()

# 使用天API
api_url = "https://apis.tianapi.com/weibohot/index?key=ab1cca5ccb089e4bed812457b6b1155a"

# 生成带日期的报告文件名（使用新命名规则）
date_str = datetime.now().strftime("%y%m%d")
time_str = datetime.now().strftime("%H%M")
output_file = f"weibo-analysis-report-{date_str}-{time_str}.html"

# 运行分析
report_path = analyzer.run_analysis(api_url)
```

### 示例2：批量分析多天数据

```python
from datetime import datetime, timedelta
from weibo_analysis import WeiboHotSearchAnalyzer

# 分析过去7天的数据
for i in range(7):
    date = datetime.now() - timedelta(days=i)
    date_str = date.strftime("%Y-%m-%d")

    analyzer = WeiboHotSearchAnalyzer()
    api_url = "https://apis.tianapi.com/weibohot/index?key=ab1cca5ccb089e4bed812457b6b1155a"

    report_path = analyzer.run_analysis(api_url)
    print(f"{date_str} 的分析完成：{report_path}")
```

### 示例3：过滤特定类型话题

```python
from weibo_analysis import WeiboHotSearchAnalyzer

class FilteredAnalyzer(WeiboHotSearchAnalyzer):
    def fetch_weibo_hot_search(self):
        # 获取所有热搜
        all_topics = super().fetch_weibo_hot_search()

        # 过滤特定标签的话题
        target_tags = ['热', '沸', '新', '荐']
        filtered_topics = [
            topic for topic in all_topics
            if topic.get('tag', '') in target_tags
        ]

        print(f"从 {len(all_topics)} 个话题中筛选出 {len(filtered_topics)} 个热门话题")
        return filtered_topics

# 使用
analyzer = FilteredAnalyzer()
analyzer.run_analysis("https://apis.tianapi.com/weibohot/index?key=ab1cca5ccb089e4bed812457b6b1155a")
```

## 🔍 故障排除

### 问题1：API返回401错误

**原因**：API Key无效或已过期
**解决**：
1. 检查API Key是否正确
2. 确认API Key未超过使用限制
3. 访问天API官网续费或获取新Key

### 问题2：API返回403错误

**原因**：请求被禁止
**解决**：
1. 检查请求频率是否过高
2. 确认API权限是否正确
3. 联系天API客服

### 问题3：API返回空数据

**原因**：接口可能暂时不可用
**解决**：
1. 检查网络连接
2. 稍后重试
3. 查看天API服务状态

### 问题4：数据格式不匹配

**原因**：天API可能更新了返回格式
**解决**：
1. 检查API文档是否有更新
2. 打印原始响应数据进行调试
3. 更新代码适配新格式

## 📞 获取API Key

如果您需要自己的API Key：

1. 访问 [天API官网](https://www.tianapi.com/)
2. 注册账户
3. 开通微博热搜接口
4. 获取API Key
5. 在代码中使用您的API Key替换示例Key

### 天API优势

- ✅ 数据准确，更新及时
- ✅ 多种热搜分类
- ✅ 支持历史数据查询
- ✅ 稳定的服务质量
- ✅ 详细的使用文档

## 📚 更多资源

- [天API官方文档](https://www.tianapi.com/document/)
- [天API控制台](https://console.tianapi.com/)
- [API调用示例](https://www.tianapi.com/sdk/)
- [技术支持](https://www.tianapi.com/help/)

---

**🎉 现在您可以使用真实的微博热搜API来运行完整的分析流程了！**

**快速开始**：
```bash
python test_with_real_api.py preview
```
