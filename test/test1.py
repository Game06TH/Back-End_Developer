import requests

url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q": "Bangkok", "appid": "your_api_key"}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(f"Temperature: {data['main']['temp']}°C")
else:
    print("Failed to retrieve data")