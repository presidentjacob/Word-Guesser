import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelnames)s - %(message)s')

def scraper(url):
    logging.debug('Attempting scraper')
    try:
        response = requests.get(url, timeout=10)
    except Exception as e:
        logging.debug('Error: ', e)
        return None

    if response != 200:
        return None

def main():
    url = 'https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/'
