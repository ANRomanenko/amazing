import requests
from bs4 import BeautifulSoup

url = ''

headers = {

}

response = requests.get(url, headers=headers)
print(response.status_code)