import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelnames)s - %(message)s')

def scraper(url):
    # Attempt to get a response from the url, exit if no response
    logging.debug('Attempting scraper')
    try:
        response = requests.get(url, timeout=10)
    except Exception as e:
        logging.debug('Error: ', e)
        return None

    if response != 200:
        return None
    
    # Create a soup in lxml
    soup = BeautifulSoup(response.text, 'lxml')

    # Find all the words
    words = soup.find('p')


def main():
    url = 'https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/'
