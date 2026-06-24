# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: HomeMaintenance
from datetime import date, timedelta
from typing import Optional, List, Dict, Any

class ValidationError(Exception):
    pass

def validate_date_input(user_str: str) -> date:
    try:
        return date.fromisoformat(user_str.strip())
    except ValueError as e:
        raise ValidationError(f"Неверный формат даты '{user_str}'. Используйте YYYY-MM-DD.") from e

def validate_positive_int(value: Any, min_val: int = 0) -> int:
    if not isinstance(value, (int, float)) or value < min_val:
        raise ValidationError("Значение должно быть положительным числом.")
    return int(value)

class HouseMaintenanceModel:
    def __init__(self):
        self.rooms: Dict[str, str] = {}
        self.works: List[Dict[str, Any]] = []
        self.executors: Dict[str, str] = {}
    
    def add_room(self, name: str, description: Optional[str] = None) -> None:
        if not name.strip(): raise ValidationError("Название помещения не может быть пустым.")
        self.rooms[name.lower().strip()] = description or ""

    def add_work(self, room_name: str, task: str, deadline_str: str, executor_id: Optional[str] = None) -> Dict[str, Any]:
        if not task.strip(): raise ValidationError("Описание работы не может быть пустым.")
        deadline = validate_date_input(deadline_str)
        work_data = {
            "room": room_name.lower().strip(),
            "task": task.strip(),
            "deadline": deadline,
            "executor_id": executor_id or None
        }
        self.works.append(work_data)
        return work_data

    def add_executor(self, name: str, contact_info: Optional[str] = None) -> None:
        if not name.strip(): raise ValidationError("Имя исполнителя не может быть пустым.")
        self.executors[name.lower().strip()] = contact_info or ""
