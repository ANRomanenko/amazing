from time import sleep
from bs4 import BeautifulSoup
import requests

# list_card = []

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}


def url():
    count = input("Выберите количество страниц для парсинга: ")
    count = int(count.strip())

    for count in range(1, count + 1):
        # sleep(1)
        url = f"https://auto.ria.com/uk/legkovie/ford/fiesta/state/kiev/?page={count}"
        print(f"Парсинг страницы № {count}\n ")

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all("div", class_="content-bar")
   
        for i in data:
            # title = i.find("div", class_="item ticket-title").get_text(strip=True).replace("Fiesta", "Fiesta ") # Обращаемся к переменной data которая содержит уже нашу карточку товара
            # price = i.find("span", class_="bold size22 green").get_text(strip=True)
            # mileage = i.find("li", class_="item-char js-race").get_text(strip=True)
            # print(title + "\n" + link + "\n" + price + "\n" + mileage + "\n\n")
            link = i.find("div", class_="item ticket-title").find("a").get("href")
            yield link
            # list_card.append(link)


def array():
    for link in url():

        response = requests.get(link, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, "lxml")
        # Здесь всего лишь одни такой контейнер и нам не нужен метод find_all достаточно find! это страница конкретной карты
        data = soup.find("div", class_="ticket-status-0")
        try:
            title = data.find("h1", class_="head").get_text(strip=True) # Название авто
        except AttributeError:
            continue
        price = data.find("strong").get_text(strip=True) # Цена
        mileage = data.find("div", class_="base-information bold").get_text(strip=True) # Пробег
        city = data.find("div", class_="item_inner").get_text(strip=True) # Город
        try:
            vin = data.find("span", class_="label-vin").get_text(strip=True) # VIN
        except AttributeError:
            continue
        engine = data.find("span",class_="argument").find_next(class_="argument").get_text(strip=True) # Объём двигателя
        color = data.find("span",class_="argument").find_next(class_="argument").find_next(class_="argument").get_text(strip=True) # Цвет
        first_registration = data.find("span",class_="argument").find_next(class_="argument").find_next(class_="argument").find_next(class_="argument").get_text(strip=True) # Первая регистрация
        last_registration = data.find("span",class_="argument").find_next(class_="argument").find_next(class_="argument").find_next(class_="argument").find_next(class_="argument").find_next(class_="argument").get_text(strip=True) # Последняя регистрация
        img_url = data.find("img", class_="outline m-auto").get("src") # Фото авто
        yield title, price, mileage, engine, vin, link, city, color, first_registration, last_registration, img_url
        # print(title + "\n" + price + "\n" + mileage + "\n" + city + "\n" + vin + "\n" + engine + "\n"
        #     + color + "\n" + first_registration + "\n" + last_registration + "\n" + img_url + "\n\n")