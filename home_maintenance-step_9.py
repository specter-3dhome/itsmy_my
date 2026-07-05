# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: HomeMaintenance
import json, sys

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки."""
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект (dict).")
        
        # Валидация структуры данных
        required_keys = ["rooms", "tasks", "workers"]
        for key in required_keys:
            if key not in data:
                print(f"Предупреждение: отсутствует ключ '{key}' в начальных данных.")
                continue
        
        return {
            "rooms": data.get("rooms", []),
            "tasks": data.get("tasks", []),
            "workers": data.get("workers", [])
        }

    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return {}
