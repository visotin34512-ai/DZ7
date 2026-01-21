import requests
# узнаем кординаты указанного города
city = input()
limit = 1
api_key = ""
api_key = "bf9e1115b23bf1ebd193e2328d09591a"
url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={api_key}"


responses = requests.get(url)
cor = responses.json()
lat = cor[-1]["lat"]
lon = cor[-1]["lon"]

# отправляем запрос на сайт о погоде
url_2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
responses = requests.get(url_2)
weather = responses.json()

# выводим данные о погоде, присланные с сайта
weather_data = {}
weather_data.update(weather["main"] | weather["wind"])
weather_data['visibility'] = weather['visibility']
weather_data['main'] = weather['weather'][0]['main']
weather_data['description'] = weather['weather'][0]['description']
for x in weather_data.items():
    print(x[0], "=", x[1])
