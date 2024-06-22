from bs4 import BeautifulSoup
import requests

url = "https://auto.ria.com/uk/legkovie/ford/fiesta/state/kiev/?page=1"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

data = soup.find("div", class_="content-bar")

title = data.find("div", class_="item ticket-title").get_text(strip=True).replace("Fiesta", "Fiesta ") # Обращаемся к переменной data которая содержит уже нашу карточку товара
print(title)