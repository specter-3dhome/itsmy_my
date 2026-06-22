# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: HomeMaintenance
import datetime as dt
from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum

class RoomType(Enum):
    KITCHEN = "кухня"
    BATHROOM = "ванная"
    LIVING_ROOM = "гостиная"

@dataclass
class Task:
    name: str
    room_type: RoomType
    scheduled_date: dt.date
    status: str = "planned"

@dataclass
class Worker:
    name: str
    skills: List[str]
    available_from: dt.date

class HomeMaintenanceApp:
    def __init__(self):
        self.tasks: List[Task] = []
        self.workers: List[Worker] = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def add_worker(self, worker: Worker) -> None:
        self.workers.append(worker)

def main():
    app = HomeMaintenanceApp()
    
    # Демонстрационные данные
    kitchen_cleaning = Task("Генеральная уборка", RoomType.KITCHEN, dt.date.today().replace(day=1))
    bathroom_maintenance = Task("Замена смесителя", RoomType.BATHROOM, dt.date.today().replace(year=today.year + 1))
    
    plumber = Worker("Иван Петров", ["сантехника", "плитка"], dt.date(2024, 1, 1))
    cleaner = Worker("Анна Сидорова", ["уборка", "химчистка"], dt.date.today())
    
    app.add_task(kitchen_cleaning)
    app.add_task(bathroom_maintenance)
    app.add_worker(plumber)
    app.add_worker(cleaner)
    
    print(f"Добавлено задач: {len(app.tasks)}")
    print(f"Добавлено исполнителей: {len(app.workers)}")

if __name__ == "__main__":
    main()
