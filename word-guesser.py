import requests
from bs4 import BeautifulSoup

def scraper(url):
    try:
        response = requests.get(url, timeout=10)
    except Exception as e:
        print('Error: ', e)
        return None

    if response != 200:
        return None

def main():
    url = 'https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/'
