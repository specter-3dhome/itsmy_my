# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: HomeMaintenance
class Reminder:
    def __init__(self, task_id, date, text):
        self.task_id = task_id
        self.date = date
        self.text = text

    def is_overdue(self):
        return datetime.now().date() > self.date

    def reminder_text(self):
        if self.is_overdue():
            return f"⚠️ Задача #{self.task_id} ({self.text}) просрочена! Срок: {self.date}"
        return f"🔔 Напоминание о задаче #{self.task_id}: {self.text}, срок — {self.date}"


class RemindersSystem:
    def __init__(self):
        self._reminders = []

    def add(self, reminder):
        self._reminders.append(reminder)

    def get_due(self):
        return [r for r in self._reminders if r.is_overdue()]

    def all_texts(self):
        return [r.reminder_text() for r in self._reminders]
