import time
from datetime import datetime
import json
import requests
from bs4 import BeautifulSoup

def get_first_news():

    # Создаём словарь заголовков!
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }

    url = "https://habr.com/ru/news/"
    host = "https://habr.com"

    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    data = soup.find_all("div", class_="tm-article-snippet tm-article-snippet")

    news_dict = {}
    for article in data:
        article_title = article.find("h2", class_="tm-title tm-title_h2").get_text(strip=True)

        article_url = host + article.find("h2", class_="tm-title tm-title_h2").find("a").get("href")
        article_id = article_url.split("/")[-2]

        # Дата и время в ISO формате!
        article_time = article.find("time").get("datetime").replace(".000Z", "")
        date_from_iso = datetime.fromisoformat(article_time)
        date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
        article_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timetuple())

        # print(f"{article_title} | {article_id} | {article_date_timestamp}")
        news_dict[article_id] = {
            "article_date_timestamp": article_date_timestamp,
            "article_title": article_title,
            "article_url": article_url
        }

    with open("habr_2.json", "w", encoding="utf-8") as file:
        json.dump(news_dict, file, indent=3, ensure_ascii=False)

def check_news_update():
    with open("habr_2.json", encoding="utf-8") as file:
        news_dict = json.load(file)

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }

    url = "https://habr.com/ru/news/"
    host = "https://habr.com"

    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    data = soup.find_all("div", class_="tm-article-snippet tm-article-snippet")

    fresh_news = {}
    for article in data:
        article_url = host + article.find("h2", class_="tm-title tm-title_h2").find("a").get("href")
        article_id = article_url.split("/")[-2]

        if article_id in news_dict:
            continue
        else:
            article_title = article.find("h2", class_="tm-title tm-title_h2").get_text(strip=True)

            # Дата и время в ISO формате!
            article_time = article.find("time").get("datetime").replace(".000Z", "")
            date_from_iso = datetime.fromisoformat(article_time)
            date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
            article_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timetuple())

            # print(f"{article_title} | {article_id} | {article_date_timestamp}")
            news_dict[article_id] = {
                "article_date_timestamp": article_date_timestamp,
                "article_title": article_title,
                "article_url": article_url
            }

            fresh_news[article_id] = {
                "article_date_timestamp": article_date_timestamp,
                "article_title": article_title,
                "article_url": article_url
            }

    with open("habr_2.json", "w", encoding="utf-8") as file:
        json.dump(news_dict, file, indent=3, ensure_ascii=False)

    return fresh_news

def main():
    # get_first_news()
    print(check_news_update())

if __name__ == "__main__":
    main()       