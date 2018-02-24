import requests
import json

KEY = 'trnsl.1.1.20180221T200547Z.5749aa3c8b24a482.d4410701318ccedb2660216709beb4e8e5189de7'
TranslateURL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
DetectURL = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
GetLangURL = 'https://translate.yandex.net/api/v1.5/tr.json/getLangs'

origin_text = ''
trans_file_directory = ''

settings = []

with open('e:/x/config/config.json') as config_file:
    settings = json.load(config_file)

def user_messege():
    print('Добро пожаловать!\n'
        'Это переводчик с русского на английский\n'
        'Для начала перевода введи "p"\n'
        'Для определения языка нажмите "d"\n'
        'Для входа в настройки нажми "s"\n'    
        'Для выхода нажми "e"\n')


def list_on_string():
    with open(settings['open_path']) as origin_text:
        s_text = []

        for x in origin_text:
            x = x.replace('\n', '')
            s_text.append(x)

        s_text = [value for value in s_text if value]
        my_srting = ''.join(s_text)
        return my_srting


def translate():

        my_string = list_on_string()

        params = {
            'key': KEY,
            'text': my_string,
            'lang': settings['translation'],
        }
        respounce = requests.get(TranslateURL, params=params)

        text = respounce.json()['text'][0]
        return text


def get_langcode(text):
    params = {
        'key': KEY,
        'text': text,
    }

    respounce = requests.get(DetectURL, params=params)
    langcode = respounce.json()['lang']

    return langcode


def get_lang(langcode):
    params = {
        'key': KEY,
        'ui': langcode,
    }

    respounce = requests.get(GetLangURL, params=params)
    answer = respounce.json()['langs'][langcode]

    return answer


def detect_sub_menu():
    user_input = input('Нажмите "w" и введите текст вручную, или нажмите "f", '
                       'чтобы получить текст из указанного файла\n')
    if user_input == 'w':
        user_input = input('Введите текст: \n')
        return user_input
    if user_input == 'f':
        my_string = list_on_string()
        return my_string


def detectlang():
    text = detect_sub_menu()

    langcode = get_langcode(text)
    lang = get_lang(langcode)

    print('Язык текста: %s\n' % lang)


def saving_file(setting, key):
    question = input('Сохранить настройки? y/n \n')
    if question == 'y':
        if key == 'i':
            settings['open_path'] = setting
        if key == 'o':
            settings['save_path'] = setting
        if key == 't':
            settings['translation'] = setting

        with open('e:/x/config/config.json', 'w') as config_file:
            json.dump(settings, config_file)
    if question == 'n':
        menu_settings()


def menu_settings_action(key_value):
    if key_value == 'i':
        input_setting = input('Укажи новый путь к файлу для перевода: \n')
        saving_file(input_setting, 'i')
    if key_value == 'o':
        input_setting = input('Укажи новый путь к файлу для сохранения: \n')
        saving_file(input_setting, 'o')
    if key_value == 't':
        input_setting = input('Укажи новое направление перевода (в формате ru-en): \n')
        saving_file(input_setting, 't')


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


def write_text_on_file(ready_text):
    with open(settings['save_path'], 'w') as file_for_saving:
        file_for_saving.write(ready_text)
    print('Готово!\n')


while True:
    user_messege()
    user_input = input()

    if user_input == 'p':
        ready_text = translate()
        write_text_on_file(ready_text)
    if user_input == 'd':
        detectlang()
    if user_input == 's':
        menu_settings()
    if user_input == 'e':
        break
