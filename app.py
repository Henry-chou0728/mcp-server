import requests
from mcp.server.fastmcp import FastMCP

# 1. 初始化 FastMCP
mcp = FastMCP("WeatherService")

# 填入你的 OpenWeatherMap API Key
API_KEY = "95faa88d5e58ce3157d96ec23745bef5"

# 2. 定義天氣查詢工具
@mcp.tool()
def get_weather(city: str) -> str:
    """
    查詢指定城市的即時天氣狀況。
    :param city: 城市名稱 (例如: "Taipei" 或 "London")
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=zh_tw"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            return f"{city} 目前的天氣是：{desc}，氣溫為 {temp}°C。"
        else:
            return f"無法查詢天氣：{data.get('message', '未知錯誤')}"
    except Exception as e:
        return f"連線發生錯誤: {str(e)}"

if __name__ == "__main__":
    mcp.run()