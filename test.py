import requests
from bs4 import BeautifulSoup
from googletrans import Translator

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


def translate_to_russian(text):
    translator = Translator()
    try:
        translated = translator.translate(text, dest='ru')
        return translated.text
    except Exception as e:
        print(f"Ошибка при переводе: {e}")
        return text

def word_game():
    print('Добро пожаловать в игру "Слова"')
    while True:
        word_dict = get_english_words()
        if not word_dict:
            print("Не удалось получить слово и определение.")
            break

        word = word_dict.get('english_words')
        word_definition = word_dict.get('word_definition')

        translated_word = translate_to_russian(word)
        translated_definition = translate_to_russian(word_definition)

        print(f'Значение слова - {translated_definition}')
        user = input('Введите слово: ')
        if user.lower() == translated_word.lower():
            print('Вы угадали слово')
            break
        else:
            print('Вы не угадали слово')
            print(f'Слово - {translated_word}')

        play_again = input('Хотите сыграть еще раз? (y/n) ')
        if play_again.lower() != 'y':
            print('Спасибо за игру')
            break

word_game()



