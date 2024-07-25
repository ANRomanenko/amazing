import json
import requests
from bs4 import BeautifulSoup

def get_first_news():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }

    url = 'https://nv.ua/allnews.html'

    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    data = soup.find_all('div', class_='row-result')
    
    new_dict = {} # создаём словатрь для наших статей и на каждой итерации будем его заполнять

    for article in data:
        article_title = article.find('div', class_='title').get_text(strip=True)
        article_url = article.find('a').get('href')
        article_date_time = article.find('span', class_='additional-pub-date').get_text(strip=True)

        article_id = article_url.split("-")[-1] # забираем последний элемент ссылки
        article_id = article_id[:-5] # обрезаем лишние символы чтобы остался только номер

        # print(f"{article_title} | {article_url} | {article_date_time}")

        new_dict[article_id] = {
            "article_title": article_title,
            "article_url": article_url,
            "article_date_time":article_date_time
        } # ключами у нас будут айдишники статей, а значения словари с собранными данными

    with open("news.json", "w", encoding='utf-8') as file:
        json.dump(new_dict, file, indent=3, ensure_ascii=False)


def check_news_update():
    with open("news.json", encoding='utf-8') as file:
        new_dict = json.load(file)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }

    url = 'https://nv.ua/allnews.html'

    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    data = soup.find_all('div', class_='row-result')

    fresh_news = {}
    for article in data:
        article_url = article.find('a').get('href')
        article_id = article_url.split("-")[-1] # забираем последний элемент ссылки
        article_id = article_id[:-5] # обрезаем лишние символы чтобы остался только номер

        if article_id in new_dict:
            continue
        else:
            article_title = article.find('div', class_='title').get_text(strip=True)
            article_date_time = article.find('span', class_='additional-pub-date').get_text(strip=True)

            new_dict[article_id] = {
                "article_title": article_title,
                "article_url": article_url,
                "article_date_time":article_date_time
            } # ключами у нас будут айдишники статей, а значения словари с собранными данными

            fresh_news[article_id] = {
                "article_title": article_title,
                "article_url": article_url,
                "article_date_time":article_date_time  
            }

    with open("news.json", "w", encoding='utf-8') as file:
        json.dump(new_dict, file, indent=3, ensure_ascii=False)

    return fresh_news

def main():
    # get_first_news()
    print(check_news_update())

if __name__ == '__main__':
    main()