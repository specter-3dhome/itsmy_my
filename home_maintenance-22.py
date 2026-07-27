# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: HomeMaintenance
def check_overdue_reminders():
    """Проверяет напоминания, которые прошли свой срок."""
    overdue = []
    for reminder in reminders:
        if datetime.now() > datetime.fromisoformat(reminder['deadline']):
            overdue.append({
                'id': reminder['id'],
                'text': reminder['text'],
                'deadline': reminder['deadline'],
                'days_overdue': (datetime.now() - datetime.fromisoformat(reminder['deadline'])).days,
            })
    if overdue:
        print(f"\n⚠️  Просрочено {len(overdue)} напоминание:")
        for item in overdue:
            print(f"  • [{item['id']}] \"{item['text']}\" — просрочено на {item['days_overdue']} дн.")


if __name__ == '__main__':
    check_overdue_reminders()
