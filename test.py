import requests
from bs4 import BeautifulSoup

url = "https://randomword.com/"

response = requests.get(url)

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        english_words = soup.find('div', id = 'random_word').text.strip()
        word_definition = soup.find('div', id = 'random_word_definition').text.strip()

        return {
            'english_words': english_words,
            'word_definition': word_definition
        }
    except:
        print(f"произошла ошибка при обращении к {url}")

def word_game():
    print(f'добро пожаловать в игру "слова"')
    while True:
        word_dict = get_english_words()
        word = word_dict.get('english_words')
        word_definition = word_dict.get('word_definition')

        print(f'значение слова - {word_definition}')
        user = input('введите слово: ')
        if user == word:
            print(f'вы угадали слово')
            break
        else:
            print(f'вы не угадали слово')
            print(f'слово - {word}')

        play_again = input('хотите сыграть еще раз? (y/n) ')
        if play_again.lower() != 'y':
            print(f'спасибо за игру')
            break

word_game()


