import requests
import json

KEY = 'trnsl.1.1.20180221T200547Z.5749aa3c8b24a482.d4410701318ccedb2660216709beb4e8e5189de7'
TranslateURL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
DetectURL = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
GetLangURL = 'https://translate.yandex.net/api/v1.5/tr.json/getLangs'

cut_text = ''
origin_text = ''
trans_file_directory = ''

settings = []

with open('e:/x/config/config.json') as config_file:
    settings = json.load(config_file)

def user_messege():
    print('welcome motherfucker!\n'
        'Это переводчик с русского на английский\n'
        'Для начала перевода введи "p"\n'
        'Для определения языка нажмите "d"\n'
        'Для входа в настройки нажми "s"\n'    
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


def translate(path):
    with open(path) as origin_text:

        s_text = []

        for x in origin_text:
            x.replace('\n', '---')
            s_text.append(x)

        #print(s_text)

        params = {
            'key': KEY,
            'text': s_text,
            'lang': settings['translation'],
        }
        respounce = requests.get(TranslateURL, params=params)

        text = respounce.json()['text'][0]

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


def menu_settings_action(key_value):
    if key_value == 'i':
        input_setting = input('Укажи новый путь к файлу для перевода: \n')
        question = input('Сохранить настройки? y/n \n')
        if question == 'y':
            settings['open_path'] = input_setting
            with open('e:/x/config/config.json', 'w') as config_file:
                json.dump(settings, config_file)
    if key_value == 'o':
        input_setting = input('Укажи новый путь к файлу для сохранения: \n')
        question = input('Сохранить настройки? y/n \n')
        if question == 'y':
            settings['save_path'] = input_setting
            with open('e:/x/config/config.json', 'w') as config_file:
                json.dump(settings, config_file)
    if key_value == 't':
        input_setting = input('Укажи новое направление перевода (в формате ru-en): \n')
        question = input('Сохранить настройки? y/n \n')
        if question == 'y':
            settings['translation'] = input_setting
            with open('e:/x/config/config.json', 'w') as config_file:
                json.dump(settings, config_file)


def menu_settings():
    while True:
        print('Меню настройки\n'
              'Текущие настройки:\n'
              'Путь к файлу с исходным текстом: "{0}" для редактирования нажми "i"\n'
              'Путь к готовому файлу: "{1}" для редактирования нажми "o"\n'
              'Направление перевода: "{2}" для редактирования нажми "t"\n'
              'Для возврата в предыдущее меню нажми "m"\n'
              .format(settings['open_path'],
                      settings['save_path'],
                      settings['translation']))

        user_input = input()

        if user_input == 'i':
            menu_settings_action('i')
        if user_input == 'o':
            menu_settings_action('o')
        if user_input == 't':
            menu_settings_action('t')
        if user_input == 'm':
            break

def write_text_on_file(file_directory, ready_text):
    with open(file_directory, 'w') as file_for_saving:
        file_for_saving.write(ready_text)


while True:
    user_messege()
    user_input = input()

    #if user_input == 'i':
    #    origin_text = translating_file()
    #if user_input == 'o':
    #    trans_file_directory = translated_file()
    if user_input == 'p':
        ready_text = translate(settings['open_path'])
        write_text_on_file(settings['save_path'], ready_text)
    if user_input == 'd':
        detectlang(cut_text)
    if user_input == 's':
        menu_settings()
    if user_input == 'e':
        break
