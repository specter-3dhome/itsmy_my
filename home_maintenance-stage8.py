# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: HomeMaintenance
import sys, os, time, datetime as dt
from typing import Optional

def print_menu():
    print("\n=== HomeMaintenance Menu ===")
    print("1. Список помещений")
    print("2. Добавить помещение")
    print("3. Показать работы по помещению")
    print("4. Назначить исполнителя на работу")
    print("5. Установить напоминание")
    print("6. Вывести список напоминаний")
    print("7. Сохранить и выйти")
    print("0. Завершить программу")

def get_int(prompt: str, min_val: int = 0) -> int:
    while True:
        try:
            val = int(input(prompt))
            if val >= min_val:
                return val
            else:
                print(f"Ошибка: введите число больше или равно {min_val}")
        except ValueError:
            print("Ошибка: введено некорректное значение")

def get_str(prompt: str) -> str:
    return input(prompt).strip()

# Глобальные хранилища (если они еще не определены, создадим их здесь для автономности блока)
if not globals().get('rooms'): rooms = {}
if not globals().get('tasks'): tasks = []
if not globals().get('workers'): workers = set()
if not globals().get('reminders'): reminders = []

def main():
    while True:
        print_menu()
        choice = get_int("\nВыберите действие (0-7): ", 0)
        
        if choice == 1: # Список помещений
            if rooms:
                for i, room in enumerate(rooms.values(), 1):
                    print(f"{i}. {room['name']} ({room.get('status', 'Новое')})")
            else:
                print("Помещений нет.")
        
        elif choice == 2: # Добавить помещение
            name = get_str("Название помещения: ")
            if not rooms or name not in rooms:
                room_id = len(rooms) + 1
                rooms[name] = {'id': room_id, 'status': 'Новое'}
                print(f"Помещение '{name}' добавлено.")
        
        elif choice == 3: # Показать работы по помещению
            if not rooms:
                print("Нет помещений.")
                continue
            name = get_str("Выберите помещение (или введите название): ")
            if name in rooms and tasks:
                room_tasks = [t for t in tasks if t.get('room') == name]
                if room_tasks:
                    for i, t in enumerate(room_tasks, 1):
                        print(f"{i}. [{t['status']}] {t['task']} - Исполнитель: {t.get('worker', 'Не назначен')}")
                else:
                    print("Работы для этого помещения не найдены.")
            else:
                print("Помещение не найдено.")
        
        elif choice == 4: # Назначить исполнителя
            if not rooms or not tasks:
                print("Недостаточно данных.")
                continue
