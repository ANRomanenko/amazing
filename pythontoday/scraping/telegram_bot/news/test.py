
# url = 'https://nv.ua/ukraine/events/otklyuchenie-sveta-v-ukrenergo-rasskazali-kak-budut-vyklyuchat-21-iyulya-50436281.html'

# article_id = url.split("-")[-1] # забираем последний элемент ссылки
# article_id = article_id[:-5] # обрезаем лишние символы чтобы остался только номер
# print(article_id)

import json

with open(r"pythontoday\scraping\telegram_bot\news.json", encoding='utf-8') as file:
    new_dict = json.load(file)

search_id = '504362823399'

if search_id in new_dict:
    print('Новость уже есть в словаре пропускаем итерацию!')
else:
    print('Свежая новость, добавляем в словарь!')