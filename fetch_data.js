const fs = require('fs');

const WEIBO_API_URL = "https://apis.tianapi.com/weibohot/index";
const WEIBO_API_KEY = "ab1cca5ccb089e4bed812457b6b1155a";

const BAIDU_SEARCH_URL = "https://qianfan.baidubce.com/v2/ai_search/web_search";
const BAIDU_API_KEY = "bce-v3/ALTAK-L6TPvDXqOGEqEIB2Ogh0z/4432bd66294ce9b19fdca57204bd2024c8e40db6";

async function getWeiboHotList() {
    console.log("Fetching Weibo Hot List...");
    try {
        const response = await fetch(`${WEIBO_API_URL}?key=${WEIBO_API_KEY}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        if (data.code === 200) {
            return data.result.list || [];
        } else {
            console.error("Error fetching Weibo data:", data);
            return [];
        }
    } catch (e) {
        console.error("Exception fetching Weibo data:", e);
        return [];
    }
}

async function searchBaidu(query) {
    console.log(`Searching Baidu for: ${query}`);
    try {
        const response = await fetch(BAIDU_SEARCH_URL, {
            method: 'POST',
            headers: {
                'X-Appbuilder-Authorization': `Bearer ${BAIDU_API_KEY}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                messages: [
                    {
                        content: `详细搜索：${query}，提供事件的完整背景、时间线和影响`,
                        role: "user"
                    }
                ]
            })
        });

        if (!response.ok) {
            console.error(`Baidu Search error: ${response.status} ${response.statusText}`);
            return null;
        }
        return await response.json();
    } catch (e) {
        console.error("Exception searching Baidu:", e);
        return null;
    }
}

async function main() {
    const hotList = await getWeiboHotList();
    if (!hotList || hotList.length === 0) {
        console.log("No hot list found.");
        return;
    }

    const results = [];
    const topN = 10;
    
    // Process top 10
    for (let i = 0; i < Math.min(hotList.length, topN); i++) {
        const item = hotList[i];
        const hotword = item.hotword;
        if (!hotword) continue;

        // Basic delay to be nice
        await new Promise(r => setTimeout(r, 1000));
        
        const searchResult = await searchBaidu(hotword);
        
        results.push({
            hotword: hotword,
            hotwordnum: item.hotwordnum,
            search_result: searchResult
        });
    }

    fs.writeFileSync('analysis_data.json', JSON.stringify(results, null, 2), 'utf8');
    console.log("Data collection complete. Saved to analysis_data.json");
}

main();
