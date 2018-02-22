import requests

KEY = 'trnsl.1.1.20180221T200547Z.5749aa3c8b24a482.d4410701318ccedb2660216709beb4e8e5189de7'
TranslateURL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
DetectURL = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
GetLangURL = 'https://translate.yandex.net/api/v1.5/tr.json/getLangs'

cut_text = ''
origin_text = ''
trans_file_directory = ''


def user_messege():
    print('welcome motherfucker!\n'
          'Это переводчик с русского на английский\n'
          'Для указания начального файла введи "i"\n'
          'Для указания дериктории для конечного файла введи "o"\n'
          'Для начала перевода введи "p"\n'
          'Для определения языка нажмите "d"\n'
          'Для выхода нажми "e"\n')


def translating_file():
    some_text = []

    usr_input = input('Укажите путь к файлу: \n')

    with open(usr_input) as user_file:
        for line in user_file:
            some_text.append(line)

    return some_text[0]


def translated_file():
    usr_input = input('Укажите директорию и имя для сохранения файла: \n')

    return usr_input


def translate(my_text):
    params = {
        'key': KEY,
        'text': my_text,
        'lang': 'ru-en',
    }
    respounce = requests.get(TranslateURL, params=params)

    text = respounce.json()['text'][0]
    cut_textline = my_text[0:20]

    detectlang(cut_textline)

    return text


def detectlang(cut_textline):
    if cut_textline != '':
        text = cut_textline
    else:
        text = input('Введите текст на исходном языке: \n')

    params = {
        'key': KEY,
        'text': text,
    }

    respounce = requests.get(DetectURL, params=params)
    langcode = respounce.json()['lang']

    params = {
        'key': KEY,
        'ui': langcode,
    }

    respounce = requests.get(GetLangURL, params=params)
    answer = respounce.json()['langs'][langcode]

    print('Язык текста: %s\n' % answer)


def write_text_on_file(file_directory, ready_text):
    with open(file_directory, 'w') as file_for_saving:
        file_for_saving.write(ready_text)


while True:
    user_messege()
    user_input = input()

    if user_input == 'i':
        origin_text = translating_file()
    if user_input == 'o':
        trans_file_directory = translated_file()
    if user_input == 'p':
        ready_text = translate(origin_text)
        write_text_on_file(trans_file_directory, ready_text)
    if user_input == 'd':
        detectlang(cut_text)
    if user_input == 'e':
        break
