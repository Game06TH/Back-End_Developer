import requests

API_key = '5f57a156689ba32e7545cd00cef49105'

city ='bangkok'

URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}'

result = requests.get(URL).json()
print(result)

city_name = result['name']
country = result['sys']['country']
weather = result['weather'][0]['main']
description = result['weather'][0]['description']
temp = result['main']['temp'] - 273.15

print(f'เมือง {city_name} ประเทศ {country}')
print(f'สภาพอากาส {weather} มีลักษณะ {description}')
print(f'อุณหภูมิ {temp } C ')