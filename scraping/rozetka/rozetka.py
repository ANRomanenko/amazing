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

        url = f'https://bt.rozetka.com.ua/ua/cookers/c80122/page={count};seller=rozetka;43169=78714/'
        print(f"Парсинг страницы №: {count}\n")

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all('li', class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")

        for i in data:

            link = i.find("a", class_="product-link goods-tile__heading").get("href")
            yield link


def rchar():

    for card in url():

        response = requests.get(card, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find('ul', class_="tabs__list")
        
        link = data.find("li", class_="tabs__item ng-star-inserted").find_next('li').find("a").get("href")
        yield link
        # with open("rozetka.html", "w", encoding="utf-8") as file:
        #     file.write(str(data))


def array():

    for char in rchar():

        response = requests.get(char, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find('rz-product-tab-characteristics', class_="ng-star-inserted")

        title = data.find("div", class_="product-carriage__goods-title").get_text(strip=True)

        try:
            price = data.find("p", class_="product-carriage__price_color-red").get_text(strip=True)
        except AttributeError:
            continue
        yield title, price, char