# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: HomeMaintenance
import unittest
from home_maintenance.models import Room, Task, Worker, Reminder, Priority, TaskStatus
from datetime import datetime, timedelta


class TestModels(unittest.TestCase):

    def test_room_creation(self):
        room = Room(name="Kitchen", area=15.0, surface="Laminate")
        self.assertEqual(room.name, "Kitchen")
        self.assertEqual(room.area, 15.0)
        self.assertEqual(room.surface, "Laminate")

    def test_task_creation(self):
        task = Task(description="Clean Kitchen", room=Room(name="Kitchen"), priority=Priority.HIGH, status=TaskStatus.PENDING)
        self.assertEqual(task.description, "Clean Kitchen")
        self.assertEqual(task.priority, Priority.HIGH)
        self.assertEqual(task.status, TaskStatus.PENDING)

    def test_worker_creation(self):
        worker = Worker(name="John", skills=["Cleaning", "Plumbing"], hourly_rate=25.0)
        self.assertEqual(worker.name, "John")
        self.assertEqual(worker.skills, ["Cleaning", "Plumbing"])
        self.assertEqual(worker.hourly_rate, 25.0)

    def test_reminder_creation(self):
        reminder = Reminder(task=Task(description="Test Task"), minutes_before=60, message="Don't forget!")
        self.assertEqual(reminder.task.description, "Test Task")
        self.assertEqual(reminder.minutes_before, 60)
        self.assertEqual(reminder.message, "Don't forget!")

    def test_priority_ordering(self):
        self.assertLess(Priority.LOW, Priority.MEDIUM)
        self.assertLess(Priority.MEDIUM, Priority.HIGH)
        self.assertLess(Priority.HIGH, Priority.URGENT)

    def test_task_status_ordering(self):
        self.assertLess(TaskStatus.PENDING, TaskStatus.IN_PROGRESS)
        self.assertLess(TaskStatus.IN_PROGRESS, TaskStatus.COMPLETED)

    def test_room_equality(self):
        room1 = Room(name="Living Room", area=20.0)
        room2 = Room(name="Living Room", area=20.0)
        self.assertEqual(room1, room2)

    def test_task_equality(self):
        task1 = Task(description="Test", room=Room(name="Test"), priority=Priority.MEDIUM, status=TaskStatus.PENDING)
        task2 = Task(description="Test", room=Room(name="Test"), priority=Priority.MEDIUM, status=TaskStatus.PENDING)
        self.assertEqual(task1, task2)


if __name__ == "__main__":
    unittest.main()
