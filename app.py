import requests

city_name = "London"
api_key = "2cd1092372c641d5f53aa7434a67a159"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},uk&APPID={api_key}"

result = requests.get(url)
data_extracted = result.json()

temp_city = data_extracted["main"]["temp"]
city_name_extracted = data_extracted["name"]

message = f"The temperature of city {city_name_extracted} is {temp_city}"

print(message)