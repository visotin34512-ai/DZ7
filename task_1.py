import requests
# Отправляем GET-запрос
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

# выводим заголовок и тело запроса 
response = response.json()
for num, post in enumerate(response[:5], start=1):
    print(num, post['title'])
    print(post['body'])






