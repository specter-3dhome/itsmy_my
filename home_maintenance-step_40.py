# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: HomeMaintenance
import argparse

def main():
    parser = argparse.ArgumentParser(description="HomeMaintenance CLI")
    sub = parser.add_subparsers(dest="cmd")
    
    p_create = sub.add_parser("add-room", help="Добавить помещение")
    p_create.add_argument("name", help="Название помещения")
    p_create.add_argument("--floor", type=int, default=1, help="Этаж")
    
    p_add_task = sub.add_parser("add-task", help="Добавить задачу")
    p_add_task.add_argument("room", help="Помещение")
    p_add_task.add_argument("description", help="Описание")
    p_add_task.add_argument("--date", help="Дата начала (YYYY-MM-DD)")
    p_add_task.add_argument("--due", help="Срок (YYYY-MM-DD)")
    p_add_task.add_argument("--priority", choices=["low","medium","high"], default="medium")
    
    p_add_worker = sub.add_parser("add-worker", help="Добавить исполнителя")
    p_add_worker.add_argument("name", help="Имя")
    p_add_worker.add_argument("phone", help="Телефон")
    
    p_add_reminder = sub.add_parser("add-reminder", help="Добавить напоминание")
    p_add_reminder.add_argument("task", help="ID задачи")
    p_add_reminder.add_argument("text", help="Текст напоминания")
    
    p_show = sub.add_parser("show", help="Просмотреть все данные")
    
    p_list = sub.add_parser("list", help="Список сущностей")
    p_list.add_argument("entity", choices=["rooms","tasks","workers","reminders"])
    
    args = parser.parse_args()
    
    if args.cmd is None:
        parser.print_help()
        return
    
    # Здесь будет подключение к хранилищу и выполнение логики.
    # Пока — демонстрация структуры CLI.
    print(f"Command: {args.cmd}")
    if hasattr(args, "name"):
        print(f"  name: {args.name}")
    if hasattr(args, "description"):
        print(f"  description: {args.description}")
    if hasattr(args, "worker_name"):
        print(f"  worker: {args.worker_name}")

if __name__ == "__main__":
    main()
