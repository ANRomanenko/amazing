import requests
import time
from datetime import datetime
import json
from bs4 import BeautifulSoup

def get_firt_news():

    headers = {

    }

    url = ""
    host = ""

    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    data = soup.find_all()

    for article in data:
        