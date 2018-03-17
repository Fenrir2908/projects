import datetime     # Библиотека для получения текущего времени и работы с ним
import sys          # Библиотека для работы с командной строкой
import os           # Библиотека для создания конечной директории
import subprocess   # Библиотека для запуска сторонних программ

DIRECTORY = []      # Создаем список для сохранения директорий

day_hour = datetime.datetime.today()        # Получаем текущую дату
today = datetime.datetime.date(day_hour)    # Убираем от даты время

args = sys.argv[:]      # Получаем аргументы коммандной строки

for i in args:
    DIRECTORY.append(i)  # Заполняем список

destination_directory = DIRECTORY[2]+str(today)+'/'        # Составляем ссылку на конечную директорию

os.mkdir(destination_directory)     # Создаем конечную директорию

subprocess.run(['C:/Program Files/7-zip/7z.exe', 'a', '-ssw', '-mx1',
                destination_directory + str('backup.7z'), DIRECTORY[1]])    # Упаковываем нужный файл через 7-zip
