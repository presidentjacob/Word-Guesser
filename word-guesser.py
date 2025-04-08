import requests
from bs4 import BeautifulSoup

def scraper(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
    except Exception as e:
        print('Error: ', e)
        return None

def main():
    url = 'https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/'
