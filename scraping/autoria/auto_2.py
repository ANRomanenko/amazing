from time import sleep
from bs4 import BeautifulSoup
import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}


def url():

    count = input("Введите количество страниц для парсинга: ")
    count = int(count.strip())

    for count in range(1, count + 1):

        url = f"https://auto.ria.com/uk/legkovie/audi/a4/state/kiev/?page={count}"
        print(f"Парсинг страницы №: {count}\n")

        response = requests.get(url, headers=headers)
        # sleep(3)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all("div", class_="content-bar")

        for i in data:
            link = i.find("div", class_="item ticket-title").find("a").get("href")
            yield link

def content():

    for card in url():

        response = requests.get(card, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find("div", class_="ticket-status-0")
        
        try:
            title = data.find("h1", class_="head").get_text(strip=True)
        except AttributeError:
            continue
        price = data.find("strong").get_text(strip=True)
        mileage = data.find("div", class_="base-information bold").get_text(strip=True).replace(" км пробіг", "")
        try:
            vin = data.find("span", class_="label-vin").get_text(strip=True)
        except AttributeError:
            continue
        img_url = data.find("img", class_="outline m-auto").get("src")
        yield title, price, mileage, vin, img_url, card
    