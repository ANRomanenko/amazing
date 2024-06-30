from time import sleep
from bs4 import BeautifulSoup
import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}



def url():

    count = input("Введите количество страниц для парсинга: ")
    count = int(count.strip())

    for count in range(1, count + 1):

        # Парсинг сайта allo (ноутбуки)
        url = f"https://allo.ua/ua/products/notebooks/p-{count}/"
        print(f"Парсинг страницы №: {count}\n")

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all("div", class_="product-card")

        for i in data:
            link = i.find("div", class_="product-card__content").find("a").get("href")
            yield link

def array():
    for card in url():

        response = requests.get(card, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find("div", class_="product-view")

        title = data.find("h1", class_="p-view__header-title").get_text(strip=True)
        code = data.find("span", class_="p-view__header-sku__code").get_text(strip=True)
        price = data.find("span", class_="sum").get_text(strip=True)
        img_url = data.find("picture", class_="main-gallery__link").find("img").get("src")
        yield title, code, price, img_url, card