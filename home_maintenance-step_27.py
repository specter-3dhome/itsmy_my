# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: HomeMaintenance
def reset_demo_data():
    """Сбрасывает все сущности в исходное демо-состояние."""
    for room in rooms:
        if room['name'] == 'Гостиная':
            room.update({'area': 30.5, 'temperature': 22.0})
        elif room['name'] == 'Кухня':
            room.update({'area': 18.0, 'temperature': 24.0})
    for task in tasks:
        if task['title'] == 'Покраска стен гостиной':
            task.update({'due_date': '2025-06-15', 'status': 'planned'})
        elif task['title'] == 'Замена фильтров кондиционера':
            task.update({'due_date': '2025-07-01', 'status': 'in_progress'})
    for worker in workers:
        if worker['name'] == 'Алексей':
            worker.update({'available': True, 'current_task': None})
        elif worker['name'] == 'Мария':
            worker.update({'available': False, 'current_task': tasks[0]['id']})
    for reminder in reminders:
        if reminder['text'] == 'Купить краску для гостиной':
            reminder.update({'date': '2025-06-14', 'done': False})
        elif reminder['text'] == 'Заказать расходные материалы':
            reminder.update({'date': '2025-07-01', 'done': True})


def clear_state():
    """Полностью очищает все данные (для тестирования)."""
    rooms.clear()
    tasks.clear()
    workers.clear()
    reminders.clear()
