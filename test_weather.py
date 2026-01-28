import requests

api_key = "55341a82040e167bb40ebb242d9b6237"
url = f"https://api.openweathermap.org/data/2.5/weather?q=Tirana&appid={api_key}&units=metric"

r = requests.get(url)
print("Status code:", r.status_code)
print("Response text:", r.text)
