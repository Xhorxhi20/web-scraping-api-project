import requests
from bs4 import BeautifulSoup
import json

# --------------------
# 1. WEB SCRAPING (News Albania)
# --------------------
news_url = "https://newsalbania.al/"
news_response = requests.get(news_url)
news_soup = BeautifulSoup(news_response.text, "html.parser")

articles = news_soup.find_all("h3")

titles = []
for article in articles:
    title = article.get_text(strip=True)
    if title:
        titles.append(title)

# --------------------
# 2. API (OpenWeatherMap - Tirana)
# --------------------
api_key = "55341a82040e167bb40ebb242d9b6237"
city = "Tirana"
weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

weather_response = requests.get(weather_url)
weather_data = weather_response.json()

temperature = weather_data["main"]["temp"]
description = weather_data["weather"][0]["description"]

weather_info = f"{description}, {temperature}°C"

# --------------------
# 3. BASHKIMI I TË DHËNAVE
# --------------------
final_data = []

for title in titles:
    final_data.append({
        "title": title,
        "city": city,
        "weather": weather_info
    })

# --------------------
# 4. RUAJTJA NË FILE JSON
# --------------------
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(final_data, f, ensure_ascii=False, indent=4)

print("Të dhënat u ruajtën me sukses në file: data.json")
