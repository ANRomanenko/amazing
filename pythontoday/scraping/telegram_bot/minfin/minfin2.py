import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime

def get_first_news():

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }

    url = "https://minfin.com.ua/news/"
    host = "https://minfin.com.ua"

    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "lxml")
        data = soup.find_all("li", class_="item")

        with open("minfin.html", "w", encoding="utf-8") as file:
            file.write(str(data))



    else:
        print("Ошибка соединения!")



def main():
    get_first_news()

if __name__ == "__main__":
    main()