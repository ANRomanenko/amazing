import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

def get_first_auto():


    # Создаём словарь заголовков
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }

    url = 'https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&categories.main.id=1&country.import.usa.not=-1&price.currency=1&top=2&abroad.not=0&custom.not=1&page=0&size=20'

    r = requests.get(url=url, headers=headers) # в параметры метода передаём url адрес и заголовки запроса

    soup = BeautifulSoup(r.text, "lxml") # Создаём объект СУПА

    data = soup.find_all("div", class_='content-bar') # собераем все параметры в список

    for article in data:
        article_title = article.find('div', class_='item ticket-title').get_text(strip=True)
        # article_desc = article.find('p', class_='descriptions-ticket').get_text(strip=True)
        article_price = article.find('span', class_='size15').get_text(strip=True)
        article_milage = article.find('li', class_='js-race').get_text(strip=True)
        article_city = article.find('li', class_='view-location').get_text(strip=True).replace("(від)", "")
        article_fuel = article.find('li', class_='item-char').find_next(class_='item-char').find_next(class_='item-char').get_text(strip=True)
        article_gearbox = article.find('li', class_='item-char').find_next(class_='item-char').find_next(class_='item-char').find_next(class_='item-char').get_text(strip=True)

        article_time = article.find('div', class_='footer_ticket').find('span').find_next('span').find_next('span').get_text(strip=True)
        date_from_iso = datetime.fromisoformat(article_time)
        date_time = datetime.strftime(date_from_iso, )

        article_url = article.find('div', class_='item ticket-title').find('a').get('href')
        print(f'{article_title} | {article_time}')

get_first_auto()