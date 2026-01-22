const fs = require('fs');

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
                        content: "你好，请回复'收到'",
                        role: "user"
                    }
                ],
                stream: false
            })
        });

        const data = await response.json();
        console.log("Keys:", Object.keys(data));
        if (data.choices) {
            console.log("Choices length:", data.choices.length);
            if (data.choices.length > 0) {
                console.log("Content:", data.choices[0].message.content);
            }
        }
        if (data.result) {
            console.log("Result:", data.result);
        }

    } catch (e) {
        console.error("Error:", e);
    }
}

testApi();
