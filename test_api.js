const https = require('https');

const API_KEY = "bce-v3/ALTAK-L6TPvDXqOGEqEIB2Ogh0z/4432bd66294ce9b19fdca57204bd2024c8e40db6";
const URL = "https://qianfan.baidubce.com/v2/ai_search/chat/completions";

async function testApi() {
    console.log("Testing API...");
    try {
        const response = await fetch(URL, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${API_KEY}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                messages: [
                    {
                        content: "Hello, please reply with 'World'",
                        role: "user"
                    }
                ],
                stream: false
            })
        });

        const text = await response.text();
        console.log("Status:", response.status);
        console.log("Body:", text);

    } catch (e) {
        console.error("Error:", e);
    }
}

testApi();
