import os
import shutil
import logging
from datetime import datetime

# Настройка логирования
logging.basicConfig(filename='project_root/logs/backup.log', level=logging.INFO)

# Создание резервной копии
def create_backup():
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f'backup_{current_time}'
    backup_path = f'project_root/backups/{backup_name}'

    # Создание резервной копии
    os.makedirs(backup_path, exist_ok=True)
    shutil.copytree('project_root/data', f'{backup_path}/data')

    logging.info(f"{datetime.now()}: Создана резервная копия {backup_name}")

create_backup()
