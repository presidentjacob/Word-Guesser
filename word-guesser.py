import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def scraper(url):
    # Attempt to get a response from the url, exit if no response
    logging.debug('Attempting scraper')
    try:
        response = requests.get(url, timeout=10)
    except Exception as e:
        logging.debug(f'Error: {e}')
        return None

    if response.status_code != 200:
        logging.debug(f'Non-200 status code: {response.status_code}')
        return None
    
    # Create a soup in lxml
    soup = BeautifulSoup(response.text, 'lxml')

    # Find all the words
    paragraphs = soup.find('div', class_='field-item even').find_all('p')

    # Get the second paragraph where all the words are held
    words = paragraphs[1].text

    # Split words based on newline
    for word in words.split('\n'):
        print(word.strip())


def main():
    url = 'https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/'
    scraper(url)

main()