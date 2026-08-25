# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: HomeMaintenance
def print_project_metrics(projects):
    """Рассчитать и вывести ключевые метрики проекта."""
    total_rooms = 0
    total_tasks = 0
    total_workers = 0
    completed_tasks = 0
    total_cost = 0.0
    for p in projects:
        total_rooms += len(p['rooms'])
        total_tasks += len(p['tasks'])
        total_workers += len(p['workers'])
        completed_tasks += sum(1 for t in p['tasks'] if t['status'] == 'completed')
        total_cost += sum(t.get('cost', 0) for t in p['tasks'] if t.get('cost'))
    print(f"Помещения: {total_rooms}")
    print(f"Задачи: {total_tasks} (выполнено: {completed_tasks})")
    print(f"Исполнители: {total_workers}")
    print(f"Общая стоимость: {total_cost:.2f}")
