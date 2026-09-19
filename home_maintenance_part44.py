# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: HomeMaintenance
import json
import os
from datetime import datetime

def backup_data_file(file_path, backup_dir="backups"):
    """Создаёт резервную копию файла данных с датой и часом."""
    if not os.path.exists(file_path):
        return f"Файл {file_path} не найден"
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.basename(file_path)
    backup_path = os.path.join(backup_dir, f"{base_name}.{timestamp}.bak")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as src:
            data = src.read()
        os.makedirs(backup_dir, exist_ok=True)
        with open(backup_path, 'w', encoding='utf-8') as dst:
            dst.write(data)
        return f"Резервная копия сохранена: {backup_path}"
    except Exception as e:
        return f"Ошибка резервного копирования: {e}"
