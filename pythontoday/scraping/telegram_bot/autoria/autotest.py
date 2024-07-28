import requests
from bs4 import BeautifulSoup


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

    for i in data:
        all = i.find("div", class_='definition-data').find_all('li')
        
        for item in all:
            print(item.text.strip())


get_first_auto()