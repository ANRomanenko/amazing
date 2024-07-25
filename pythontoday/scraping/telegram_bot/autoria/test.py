# url = 'https://auto.ria.com/uk/auto_skoda_kodiaq_36900200.html'

# article_id = url.split('_')[-1]
# article_id = article_id[:-5]
# print(article_id)

import json

with open('news_dict.json', encoding='utf-8') as file:
    news_dict = json.load(file)

news = '35825218353'

if news in news_dict:
    print('Эта статься уже имеется в этом словаре. Пропускаем итерацию!')
else:
    print('Добавить новую статью!')