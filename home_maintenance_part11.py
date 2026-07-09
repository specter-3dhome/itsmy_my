# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: HomeMaintenance
import json, os

DATA_FILE = "home_maintenance.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"rooms": [], "tasks": [], "workers": [], "reminders": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for key in ["rooms", "tasks", "workers", "reminders"]:
                if key not in data:
                    data[key] = []
            return data
    except (json.JSONDecodeError, OSError):
        return {"rooms": [], "tasks": [], "workers": [], "reminders": []}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
