import time
from datetime import datetime
import json
import requests
from bs4 import BeautifulSoup

def get_first_news():

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }

    url = "https://minfin.com.ua/news/"
    host = "https://minfin.com.ua"

    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    data = soup.find_all("li", class_="item")

    news_dict = {}
    for item in data:
        try:
            item_title = item.find("span", class_="link").get_text(strip=True)
            
            item_time = item.find("span", class_="data").get("content")
            date_from_iso = datetime.fromisoformat(item_time)
            date_time = datetime.strftime(date_from_iso, "%Y-%d-%m %H:%M:%S")
            item_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%d-%m %H:%M:%S").timetuple())

            item_url = host + item.find('a').get('href')
            item_id = item_url.split('/')[-2]
        except AttributeError:
            continue
        
        # print(f"{item_date_timestamp}")
        news_dict[item_id] = {
            "item_date_timestamp": item_date_timestamp,
            "item_title": item_title,
            "item_url": item_url
        }

    with open("minfin2.json", "w", encoding="utf-8") as f:
        json.dump(news_dict, f, indent=3, ensure_ascii=False)


def check_news_update():
    with open("minfin2.json", encoding="utf-8") as f:
        news_dict = json.load(f)
    print(news_dict)
    
def main():
    # get_first_news()
    check_news_update()

if __name__ == "__main__":
    main()
