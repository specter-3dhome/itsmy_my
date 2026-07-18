# === Stage 17: Добавь группировку записей по категориям ===
# Project: HomeMaintenance
from collections import defaultdict


class CategoryGroup:
    def __init__(self, name):
        self.name = name
        self.entries = []

    def add(self, record):
        self.entries.append(record)

    def summary(self):
        return {"name": self.name, "count": len(self.entries), "records": self.entries}


class MaintenanceCategorizer:
    CATEGORIES = {
        "Ремонтные работы": ["Покраска стен", "Укладка плитки", "Монтаж труб", "Электромонтаж"],
        "Сантехнические работы": ["Установка смесителя", "Замена унитаза", "Прочистка канализации"],
        "Косметический ремонт": ["Мытье окон", "Полы", "Обои", "Карнизы"],
        "Сезонное обслуживание": ["Очистка gutters", "Проверка системы отопления", "Замена фильтров"],
    }

    def categorize(self, record):
        for cat_name, tasks in self.CATEGORIES.items():
            if task in tasks:
                return CategoryGroup(cat_name)
        return CategoryGroup("Прочее")
