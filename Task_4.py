import os  # Добавлен импорт os
import json
from pathlib import Path
from datetime import datetime


# Сбор информации о файлах
def collect_file_info():
    file_info = []

    for filename in os.listdir('project_root/data/processed'):
        filepath = Path(f'project_root/data/processed/{filename}')

        if filepath.is_file():
            stats = os.stat(filepath)
            file_info.append({
                "filename": filename,
                "size_in_bytes": stats.st_size,
                "last_modified": datetime.fromtimestamp(stats.st_mtime).isoformat()
            })

    with open('project_root/output/file_info.json', 'w', encoding='utf-8') as json_file:
        json.dump(file_info, json_file, ensure_ascii=False, indent=4)


collect_file_info()
