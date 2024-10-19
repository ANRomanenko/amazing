import csv
import requests
from bs4 import BeautifulSoup

url_main = "https://www.lego.com"
url_themes = "https://www.lego.com/en-us/themes"


def get_soup(url, page=1):
    if page == 1:
        response = requests.get(url=url)
    else:
        url = f'{url}?page={page}&offset=0'
        response = requests.get(url=url)

    with open(file='index.html', mode='w', encoding="utf-8") as file:
        file.write(response.text)

    return BeautifulSoup(response.text, "lxml")

def get_themes(soup):
    themes = soup.find('section', class_="LayoutSectionstyles__Layout-sc-1ny73ll-0 kgfysw").ul
    themes = themes.find_all('li')

    themes_list = []
    
    for theme in themes:
        themes_dict = {
            'name': theme.h2.span.text,
            'url': f'{url_main}{theme.a.get("href")}'
        }

        themes_list.append(themes_dict)

    # Проверяем, что список не пустой, прежде чем записывать в CSV
    if themes_list:
        keys = themes_list[0].keys()
        with open('themes.csv', 'w', newline='', encoding="utf-8") as file:
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(themes_list)
    else:
        print("No themes data found.")

    return themes_list

def get_toys_pages(soup):
    try:
        n_toys = int(soup.select('span[data-value]')[0].get('data-value'))
    except IndexError:
        n_toys = 0  # если не удалось найти количество игрушек
    n_pages = (n_toys // 18) + 1 if n_toys else 0

    return n_toys, n_pages

def get_toys_info(toy_data):
    t_data = {
        'age': None,
        'pieces': None,
        'rating': None
    }

    for d in toy_data:
        if '+' in d:
            t_data['age'] = d
        elif '.' in d:
            t_data['rating'] = d
        else:
            t_data['pieces'] = d

    return t_data

def get_price(toy):
    try:
        price_div = toy.find('div', {'data-test': 'product-leaf-price-row'}).text
        t_price = toy.find('span', {'data-test': 'product-leaf-price'}).text
        if '%' in price_div:
            t_discount = toy.find('span', {'data-test': 'product-leaf-discount-badge'}).text
            return t_price, t_discount
        else:
            return t_price, 0
    except AttributeError:
        return None, None

def get_toys_values(collection='Marvel'):
    with open(file='index.html', encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    toys = soup.find_all('li', {'data-test': 'product-item'})

    toys_data = []
    for toy in toys:
        try:
            toy_name = toy.find('h3').text
        except AttributeError:
            continue

        toy_data = [item.text.strip() for item in toy.find("div", {'data-test': 'product-leaf-attributes-row'}).find_all('span')]
        toy_data = get_toys_info(toy_data=toy_data)

        price, discount = get_price(toy)
        if not price:
            continue

        toy_info = {
            'name': toy_name,
            'collection': collection,
            'age': toy_data['age'],
            'pieces': toy_data['pieces'],
            'rating': toy_data['rating'].replace(".",".."),
            'price': price,
            'discount': discount
        }

        toys_data.append(toy_info)

    # Проверяем, что данные есть, прежде чем записывать в CSV
    if toys_data:
        keys = toys_data[0].keys()
        with open('toys_data.csv', 'w', newline='', encoding="utf-8") as file:
            dict_writer = csv.DictWriter(file, keys, delimiter=';')
            dict_writer.writeheader()
            dict_writer.writerows(toys_data)
    else:
        print("No toys data found.")

    return toys_data

def main():
    # Пример получения данных о темах
    # soup = get_soup(url=url_themes)
    # themes = get_themes(soup=soup)
    # print(themes)

    # Пример получения количества страниц с игрушками
    # soup = get_soup(url="https://www.lego.com/en-us/themes/disney")
    # print(get_toys_pages(soup=soup))

    # Пример получения данных об игрушках
    # soup = get_soup(url="https://www.lego.com/en-us/themes/marvel")
    get_toys_values()


if __name__ == "__main__":
    main()
