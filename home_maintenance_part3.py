# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: HomeMaintenance
from typing import Dict, List, Optional
import uuid
from datetime import datetime, timedelta

class MaintenanceRecord:
    def __init__(self, room_id: str, task_name: str, executor_name: str, due_date: datetime):
        self.id = str(uuid.uuid4())
        self.room_id = room_id
        self.task_name = task_name
        self.executor_name = executor_name
        self.due_date = due_date

class HomeMaintenanceDB:
    def __init__(self):
        self.records: List[MaintenanceRecord] = []
    
    def add_record(self, room_id: str, task_name: str, executor_name: str, 
                   days_until_due: int) -> MaintenanceRecord:
        due_date = datetime.now() + timedelta(days=days_until_due)
        record = MaintenanceRecord(room_id, task_name, executor_name, due_date)
        self.records.append(record)
        return record
    
    def get_upcoming_tasks(self, limit: int = 5) -> List[MaintenanceRecord]:
        now = datetime.now()
        future_records = [r for r in self.records if r.due_date > now]
        future_records.sort(key=lambda x: x.due_date)
        return future_records[:limit]

db = HomeMaintenanceDB()
