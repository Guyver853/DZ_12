import os
import json
from pathlib import Path
from datetime import datetime  # Добавлен импорт datetime


# Чтение и обработка данных
def process_files():
    for filename in os.listdir('project_root/data/raw'):
        filepath = Path(f'project_root/data/raw/{filename}')

        # Проверка, является ли файл текстовым
        if filepath.is_file() and filepath.suffix in ['.txt']:
            with open(filepath, 'r', encoding='utf-8' if filepath.name.endswith('utf8.txt') else 'iso-8859-1') as file:
                content = file.read()
                processed_content = content.swapcase()  # Замена регистра
                processed_filename = f'project_root/data/processed/{filepath.stem}_processed{filepath.suffix}'

                with open(processed_filename, 'w', encoding='utf-8') as processed_file:
                    processed_file.write(processed_content)


process_files()


# Сериализация данных в JSON
def serialize_to_json():
    processed_data = []

    for filename in os.listdir('project_root/data/processed'):
        filepath = Path(f'project_root/data/processed/{filename}')

        if filepath.is_file():
            stats = os.stat(filepath)
            with open(filepath, 'r', encoding='utf-8') as f:
                original_text = f.read()

            processed_data.append({
                "filename": filename,
                "original_text": original_text,
                "size_in_bytes": stats.st_size,
                "last_modified": datetime.fromtimestamp(stats.st_mtime).isoformat()  # Используется datetime
            })

    with open('project_root/output/processed_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(processed_data, json_file, ensure_ascii=False, indent=4)


serialize_to_json()
