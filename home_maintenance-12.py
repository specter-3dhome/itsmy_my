# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: HomeMaintenance
import json, os


def load_from_json(path):
    if not os.path.exists(path):
        print(f"Файл {path} не найден")
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            result = {"rooms": [], "tasks": [], "workers": [], "reminders": []}
            for item in data:
                for key in ("room", "task", "worker", "reminder"):
                    if key in item:
                        result[key] = item.get(key, [])
        return result
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return {}
