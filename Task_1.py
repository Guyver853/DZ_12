import os
import logging
from datetime import datetime


# Создание структуры директорий
def create_directories():
    directories = [
        "project_root/data/raw",
        "project_root/data/processed",
        "project_root/logs",
        "project_root/backups",
        "project_root/output"
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Создана директория {directory}")


create_directories()

# Настройка логирования (после создания директорий)
logging.basicConfig(filename='project_root/logs/file_creation.log', level=logging.INFO)

# Запись в лог о создании директорий
for directory in os.listdir("project_root"):
    if directory in ['data', 'logs', 'backups', 'output']:
        logging.info(f"{datetime.now()}: Создана директория {directory}")


# Создание и запись данных в файлы с разными кодировками
def create_files():
    content = {
        "utf8.txt": "Привет, мир!",
        "iso.txt": "Hola, mundo!"
    }
    for filename, text in content.items():
        with open(f'project_root/data/raw/{filename}', 'w',
                  encoding='utf-8' if filename.endswith('utf8.txt') else 'iso-8859-1') as f:
            f.write(text)
            logging.info(f"{datetime.now()}: Создан файл {filename}")


create_files()
