import json
import requests
from bs4 import BeautifulSoup


def get_first_news():

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }

    urlik = ["https://prom.ua/ua/Avto-moto", "https://prom.ua/ua/Odezhda", "https://prom.ua/ua/Tehnika-i-elektronika"]
    host = "https://prom.ua"

    news_dict = {}
    
    for url in urlik:
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")

        data = soup.find_all("div", class_="l-GwW js-productad")
        
        # with open("prom.html", "w", encoding="utf-8") as file:
        #     file.write(str(data))
        
        for product in data:
            product_title = product.find("div", class_="M3v0L DUxBc sMgZR _5R9j6 wEofQ qzGRQ IM66u J5vFR hxTp1").find("a").get("title")

            product_url = host + product.find("a", class_="_0cNvO jwtUM").get("href")
            product_id = product_url.split("-")[0]
            product_id = product_id.split("/")[-1]

            product_price = product.find("span", class_="yzKb6").get_text(strip=True) + " грн."
            product_delivery = product.find("div", class_="M3v0L Qa-Dw mpcTk _0Jq1n _0pTfu Oxjl- NR0J4 MuCm8 -Tr65").get_text(strip=True)
            product_company = product.find("span", class_="_3Trjq aXB7S").get_text(strip=True)

            # print(f"{product_title} | {product_price} | {product_id} | {product_delivery} | {product_company}")
            # print(f"{product_url}")
            news_dict[product_id] = {
                "product_title": product_title,
                "product_price": product_price,
                "product_delivery": product_delivery,
                "product_company": product_company,
                "product_url": product_url
            }

    with open("prom.json", "w", encoding="utf-8") as file:
        json.dump(news_dict, file, indent=5, ensure_ascii=False)


def check_news_update():
    with open("prom.json", encoding="utf-8") as file:
        news_dict = json.load(file)

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }

    url = "https://prom.ua/ua/Avto-moto"
    host = "https://prom.ua"

    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    data = soup.find_all("div", class_="l-GwW js-productad")

    fresh_news = {}
    for product in data:
        product_url = host + product.find("a", class_="_0cNvO jwtUM").get("href")
        product_id = product_url.split("-")[0]
        product_id = product_id.split("/")[-1]

        if product_id in news_dict:
            continue
        else:
            product_title = product.find("div", class_="M3v0L DUxBc sMgZR _5R9j6 wEofQ qzGRQ IM66u J5vFR hxTp1").find("a").get("title")
            product_price = product.find("span", class_="yzKb6").get_text(strip=True) + " грн."
            product_delivery = product.find("div", class_="M3v0L Qa-Dw mpcTk _0Jq1n _0pTfu Oxjl- NR0J4 MuCm8 -Tr65").get_text(strip=True)
            product_company = product.find("span", class_="_3Trjq aXB7S").get_text(strip=True)

            # print(f"{product_title} | {product_price} | {product_id} | {product_delivery} | {product_company}")
            # print(f"{product_url}")
            news_dict[product_id] = {
                "product_title": product_title,
                "product_price": product_price,
                "product_delivery": product_delivery,
                "product_company": product_company,
                "product_url": product_url
            }

            fresh_news[product_id] = {
                "product_title": product_title,
                "product_price": product_price,
                "product_delivery": product_delivery,
                "product_company": product_company,
                "product_url": product_url
            }

    with open("prom.json", "w", encoding="utf-8") as file:
        json.dump(news_dict, file, indent=5, ensure_ascii=False)   

    return fresh_news    

def main():
    # get_first_news()
    print(check_news_update())

if __name__ == "__main__":
    main()