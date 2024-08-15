# url = "https://habr.com/ru/news/835462/"

# article_id = url.split("/")[-2]
# print(article_id)


import json

with open("habr.json", encoding="utf-8") as file:
    news_dict = json.load(file)

search_id = "8359364"

if search_id in news_dict:
    print("Пропускаем новость так как она уже есть в словаре!")
else:
    print("Добавляем новую статью!")