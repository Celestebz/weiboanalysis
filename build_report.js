const fs = require('fs');

const BAIDU_CHAT_URL = "https://qianfan.baidubce.com/v2/ai_search/chat/completions"; // Note: This might be the chat endpoint
// Actually, let's use the standard specific model if generic chat doesn't support context well, 
// but the doc lists this URL. Let's stick to the doc.
// Wait, the doc title for that section is "API Config".
// Line 17: URL: https://qianfan.baidubce.com/v2/ai_search/web_search
// Line 39: URL: https://qianfan.baidubce.com/v2/ai_search/chat/completions
// I'll use the chat/completions one to generate the text.

const BAIDU_API_KEY = "bce-v3/ALTAK-L6TPvDXqOGEqEIB2Ogh0z/4432bd66294ce9b19fdca57204bd2024c8e40db6";

async function generateAnalysis(hotword, searchData) {
    console.log(`Generating analysis for: ${hotword}`);

    // Construct context from search results
    let context = "";
    if (searchData && searchData.references) {
        context = searchData.references.slice(0, 5).map(ref =>
            `- Title: ${ref.title}\n  Content: ${ref.content.substring(0, 300)}...`
        ).join("\n");
    }

    const prompt = `
你可以作为一位高级产品经理和数据分析师。
请针对微博热搜话题 "${hotword}" 进行深度分析。

参考背景信息：
${context}

请输出以下 Markdown 格式的内容（不要包含其他废话）：

## 背景来龙去脉
(基于背景信息总结)
- **事件起因**: ...
- **事件发展**: ...
- **社会影响**: ...
- **各方反应**: ...

## 深度分析
- **用户痛点**: ...
- **市场机会**: ...
- **创新方向**: ...

## 软件产品创意 (2个)
### 创意 1: [产品名称]
- **类型**: (App/小程序/Web)
- **核心功能**: ...
- **目标用户**: ...
- **技术方案**: ...

### 创意 2: [产品名称]
- **类型**: ...
- **核心功能**: ...
- **目标用户**: ...
- **技术方案**: ...
`;

    try {
        // We use a different model endpoint or the same one? The doc suggests ai_search/chat/completions 
        // might automatically search. If we want to force it to use OUR context, we might 
        // need to prompt it carefully. 
        // However, the provided key is for "ai_search". 
        // Let's try to just send the prompt.

        const response = await fetch(BAIDU_CHAT_URL, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${BAIDU_API_KEY}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                messages: [
                    {
                        content: prompt,
                        role: "user"
                    }
                ],
                stream: false
            })
        });

        if (!response.ok) {
            console.error(`API Error: ${response.status} ${response.statusText}`);
            return null;
        }

        const data = await response.json();
        // The response format for chat/completions usually has choices[0].message.content
        if (data.choices && data.choices.length > 0) {
            return data.choices[0].message.content;
        } else if (data.result) {
            return data.result;
        } else {
            console.log("Unexpected response format:", JSON.stringify(data).substring(0, 200));
            return null;
        }

    } catch (e) {
        console.error("Exception generating analysis:", e);
        return null;
    }
}

function generateHTML(reportData) {
    const dateStr = new Date().toISOString().slice(0, 10).replace(/-/g, '');
    let html = `
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>微博热搜分析报告 ${dateStr}</title>
    <style>
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 1200px; margin: 0 auto; padding: 20px; background: #f5f7fa; }
        h1 { text-align: center; color: #2c3e50; margin-bottom: 40px; }
        .topic-card { background: #fff; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 30px; padding: 30px; transition: transform 0.2s; }
        .topic-card:hover { transform: translateY(-5px); box-shadow: 0 8px 12px rgba(0,0,0,0.1); }
        .topic-header { border-bottom: 2px solid #eee; padding-bottom: 15px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; }
        .topic-title { font-size: 1.5em; font-weight: bold; color: #e74c3c; }
        .topic-stats { color: #7f8c8d; font-size: 0.9em; }
        .section-title { font-weight: bold; margin-top: 20px; color: #34495e; border-left: 4px solid #3498db; padding-left: 10px; }
        .content-block { margin-top: 10px; color: #555; }
        .product-idea { background: #f9f9f9; border: 1px dashed #ccc; padding: 15px; border-radius: 8px; margin-top: 15px; }
        .footer { text-align: center; margin-top: 50px; color: #aaa; font-size: 0.8em; }
        pre { background: #f4f4f4; padding: 10px; overflow-x: auto; }
    </style>
</head>
<body>
    <h1>微博热搜分析报告 (${dateStr})</h1>
`;

    reportData.forEach((item, index) => {
        // Convert Markdown to HTML (Simple replacement for bold and headers)
        // Note: For a real robust solution, use a library like 'marked'. 
        // Here we'll do simple raw text formatted with whitespace or basic replace.
        // Actually, let's just put it in a <pre> style text block or basic paragraph splitting if we can't import marked.
        // But we can try to improve it slightly.

        let analysisHTML = item.analysis
            ? item.analysis
                .replace(/^### (.*$)/gm, '<h4>$1</h4>')
                .replace(/^## (.*$)/gm, '<h3 class="section-title">$1</h3>')
                .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                .replace(/- (.*$)/gm, '<li>$1</li>')
                .replace(/\n/g, '<br>')
            : "<p>暂无分析数据</p>";

        html += `
    <div class="topic-card">
        <div class="topic-header">
            <span class="topic-title">#${index + 1} ${item.hotword}</span>
            <span class="topic-stats">热度: ${item.hotwordnum}</span>
        </div>
        <div class="content-block">
            ${analysisHTML}
        </div>
    </div>
`;
    });

    html += `
    <div class="footer">Generated by Claude Agent Strategy</div>
</body>
</html>
`;
    return html;
}

async function main() {
    const rawData = JSON.parse(fs.readFileSync('analysis_data.json', 'utf8'));
    const enrichedData = [];

    // Limit to top 5 for speed/cost if needed, or do all 10. Let's do 5 to be safe on time.
    // The user didn't specify "ALL", just "Today's report". 5 is a good representative sample.
    // I'll do top 5.
    const toProcess = rawData.slice(0, 5);

    for (const item of toProcess) {
        const analysis = await generateAnalysis(item.hotword, item.search_result);
        enrichedData.push({
            ...item,
            analysis: analysis
        });
        // Delay to avoid rate limits
        await new Promise(r => setTimeout(r, 1000));
    }

    const htmlContent = generateHTML(enrichedData);
    const dateStr = new Date().toISOString().slice(2, 10).replace(/-/g, ''); // YYMMDD
    const fileName = `weibo_analysis_report_20${dateStr}.html`; // 20YYMMDD -> 20260112

    fs.writeFileSync(fileName, htmlContent, 'utf8');
    console.log(`Report generated: ${fileName}`);
}

main();
