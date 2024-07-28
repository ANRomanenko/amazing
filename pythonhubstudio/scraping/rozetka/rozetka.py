import requests
from bs4 import BeautifulSoup

def content():

    count = input('Введите число страниц для парсинга: ')
    count = int(count.strip())

    # Создаём цикл который будет пробигатся по определённым страницам
    for count in range(1, count + 1): # диапазон который мы задаём в переменной count

        # Создаём словарь заголовков
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        }

        url = f'https://rozetka.com.ua/ua/mobile-phones/c80003/page={count};seller=rozetka/'
        print(f'Парсинг страницы №: {count}\n')

        r = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(r.text, "lxml")

        data = soup.find_all("div", class_="goods-tile__inner")
        
        for goods in data:
            goods_url = goods.find('a', class_='product-link goods-tile__heading').get('href')
            print(goods_url)

content()
