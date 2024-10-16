import csv
import requests
from bs4 import BeautifulSoup

url_main = "https://www.lego.com"
url_themes = "https://www.lego.com/en-us/themes"


def get_soup(url):
    respose = requests.get(url=url)

    return BeautifulSoup(respose.text, "lxml")


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

    keys = themes_list[0].keys()

    with open('themes.csv', 'w', encoding="utf-8") as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(themes_list)

    return themes_list

def main():
    soup = get_soup(url=url_themes) # функция вернет нам объект бьютифул супа
    themes = get_themes(soup=soup)
    # print(themes)

if __name__ == "__main__":
    main()