import requests
from bs4 import BeautifulSoup


def get_and_parse(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")


def flatten(t):
    return [item for sublist in t for item in sublist]


def parse_float(number: str):
    cleaned = clean_str(number)
    return None if not cleaned else float(number)


def parse_int(number: str):
    cleaned = clean_str(number)
    return None if not cleaned else int(number)


def clean_str(text: str):
    cleaned = text.strip()
    return None if cleaned == '' else cleaned
