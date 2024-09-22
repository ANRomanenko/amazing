import json

with open("minfin2.json", encoding="utf8") as f:
    news_dict = json.load(f)

article_id = "1360799699"

if article_id in news_dict:
    print("Пропускаем новость так как она есть")

else:
    print("Такой новости нет добавляем!")