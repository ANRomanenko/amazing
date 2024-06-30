from time import sleep
from bs4 import BeautifulSoup
import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}


def url():

    for count in range(1, 2 + 1):

        url = f"https://brain.com.ua/category/Telefony_mobylnye-c1274/page={count}/"
        host = "https://brain.com.ua"
        print(f"Парсинг страницы №: {count}\n")

        response = requests.get(url, headers=headers)
        # sleep(3)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all("div", class_="col-lg-3 col-md-4 col-sm-6 col-xs-6 product-wrapper br-pcg-product-wrapper")

        for i in data:
            link = host + i.find("h3", class_="br-pp-desc br-pp-ipd-hidden").find("a").get("href")
            yield link


def array():
    for card in url():

        response = requests.get(card, headers=headers)
        # sleep(3)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find("div", class_="br-body br-body-product")
        
        title = data.find("h1").get_text(strip=True)
        price = data.find("div", class_="br-pr-np").find("span").find_next("span").get("content")
        code_id = data.find("div", class_="product-code-num").find("span").get_text(strip=True)
        yield title, price, code_id, card

# spam = 0

# while spam < 5:
#     print("Hello word")
#     spam = spam + 1