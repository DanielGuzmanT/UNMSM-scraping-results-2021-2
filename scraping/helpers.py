import requests
from bs4 import BeautifulSoup


def get_and_parse(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")
