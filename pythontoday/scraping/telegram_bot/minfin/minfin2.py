import requests
import json
import time
from bs4 import BeautifulSoup
from datetime import datetime

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
    
    for item in data:
        item_title = item.find("", class_="")
        item_date = item.find("", class_="")



def main():
    get_first_news()


if __name__ == "__main__":
    main()