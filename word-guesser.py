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

    # Get the random word
    word = sheet[f'A{word_place}'].value
    length = len(word)

    wrong_guesses = 0

    # Setup a win condition
    right_letters = []
    game_won = False
    
    # Start the game
    while wrong_guesses < 5 and game_won == False:
        # Print game
        while True:
            for i in range(length):
                if word[i] in right_letters:
                    print(f'{word[i]} ', end='')
                else:
                    print('_ ', end='')
            print()
            
            # Ensure that only 1 character is entered
            guess = input('Enter in a single character: ')
            if len(guess) == 1:
                break
            print('Try again, please only one character.')

        # Add letter if it is in word and not in right_letters
        if guess in word and guess not in right_letters:
            # Append letter to right_letters
            right_letters.append(guess)
            print()

            # Check to see if the game has been won
            game_won = all(letter in right_letters for letter in word)
        # IF word is in right_letters, continue
        elif guess in right_letters:
            print('You already tried this letter!\n')
        # If wrong letter, add to wrong_guesses
        else:
            print('Sorry! That is not the correct letter!\n')
            wrong_guesses += 1

    if wrong_guesses == 5:
        print(f'Sorry! You did not get the word! It was {word}.')
    else:
        print(f'You got it! The word was {word}!')


def main():
    scraper()
    game()

main()