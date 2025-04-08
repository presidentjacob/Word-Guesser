import requests
from bs4 import BeautifulSoup
import logging
import openpyxl
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
book_name = 'thousand_words.xlsx'
url = 'https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/'

def scraper():
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

    # Create a workbook to write to
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'Words'

    # Split words based on newline
    for index, word in enumerate(words.split('\n')):
        sheet[f'A{index+1}'] = word.strip()
    
    wb.save(book_name)

def game():
    logging.debug('In game')

    # Open the workbook and grab a random word
    wb = openpyxl.load_workbook(book_name)
    sheet = wb.active
    word_place = random.randint(1, 1000)

    word = sheet[f'A{word_place}']
    length = word.len()

    print('_' * length)



def main():
    scraper()
    game()

main()