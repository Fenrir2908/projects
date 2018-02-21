import requests

KEY = 'trnsl.1.1.20180221T200547Z.5749aa3c8b24a482.d4410701318ccedb2660216709beb4e8e5189de7'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def user_messege():
    print('welcome motherfucker!\n'
        'Это переводчик с русского на английский\n'
        'Для указания начального файла введи "i"\n'
        'Для указания дериктории для конечного файла введи "o"\n'
        'Для начала перевода введи "p"\n'
        'Для выхода нажми "e"\n')

def translating_file():
    some_text = []

    user_input = input()

    with open(user_input) as user_file:
        for line in user_file:
           some_text.append(line)

    return some_text[0]

def translated_file():
    user_input = input()

    return user_input

def translate(my_text):
    params = {
        'key':KEY,
        'text':my_text,
        'lang':'ru-en',
    }
    respounce = requests.get(URL,params=params)
    return respounce.json()['text'][0]

def write_text_on_file(translated_file_directory, ready_text):
    with open(translated_file_directory, 'w') as file_for_saving:
        file_for_saving.write(ready_text)

while True:
    user_messege()
    user_input = input()

    if user_input == 'i':
        my_text = translating_file()
    if user_input == 'o':
        translated_file_directory = translated_file()
    if user_input == 'p':
        ready_text = translate(my_text)
        write_text_on_file(translated_file_directory, ready_text)
