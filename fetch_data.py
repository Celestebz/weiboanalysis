import requests
import json
import time

# Configurations
WEIBO_API_URL = "https://apis.tianapi.com/weibohot/index"
WEIBO_API_KEY = "ab1cca5ccb089e4bed812457b6b1155a"

BAIDU_SEARCH_URL = "https://qianfan.baidubce.com/v2/ai_search/web_search"
BAIDU_API_KEY = "bce-v3/ALTAK-L6TPvDXqOGEqEIB2Ogh0z/4432bd66294ce9b19fdca57204bd2024c8e40db6"

def get_weibo_hot_list():
    print("Fetching Weibo Hot List...")
    try:
        response = requests.get(WEIBO_API_URL, params={"key": WEIBO_API_KEY})
        response.raise_for_status()
        data = response.json()
        if data.get("code") == 200:
            return data.get("result", {}).get("list", [])
        else:
            print(f"Error fetching Weibo data: {data}")
            return []
    except Exception as e:
        print(f"Exception fetching Weibo data: {e}")
        return []

def search_baidu(query):
    print(f"Searching Baidu for: {query}")
    headers = {
        "X-Appbuilder-Authorization": f"Bearer {BAIDU_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "messages": [
            {
                "content": f"详细搜索：{query}，提供事件的完整背景、时间线和影响",
                "role": "user"
            }
        ]
    }
    
    try:
        response = requests.post(BAIDU_SEARCH_URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Exception searching Baidu: {e}")
        return None

def main():
    hot_list = get_weibo_hot_list()
    if not hot_list:
        print("No hot list found.")
        return

    # Process top 10
    results = []
    for item in hot_list[:10]:
        hotword = item.get("hotword")
        if not hotword:
            continue
            
        search_result = search_baidu(hotword)
        
        entry = {
            "hotword": hotword,
            "hotwordnum": item.get("hotwordnum"),
            "search_result": search_result
        }
        results.append(entry)
        time.sleep(1) # Be nice to API

    with open("analysis_data.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print("Data collection complete. Saved to analysis_data.json")

if __name__ == "__main__":
    main()
