# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: HomeMaintenance
class RecommendationEngine:
    def __init__(self):
        self.rules = [
            Rule("room", "needs_inspection", "Inspect this room soon", "pending"),
            Rule("room", "clean", "Clean this room", "dirty"),
            Rule("task", "overdue", "Do this task immediately", "overdue"),
            Rule("task", "scheduled", "Start this task", "scheduled"),
            Rule("worker", "available", "Assign this worker to a task", "available"),
        ]
    
    def get_recommendations(self, state):
        recs = []
        for rule in self.rules:
            room, status, action, priority = rule
            if room == "room" and status == "needs_inspection":
                recs.append(f"🔍 Inspect {state['rooms'][0]['name']} — status: {state['rooms'][0]['status']}")
            elif room == "room" and status == "clean":
                recs.append(f"🧹 Clean {state['rooms'][0]['name']} — status: {state['rooms'][0]['status']}")
            elif task and task["status"] == "overdue":
                recs.append(f"⏰ Overdue task: {task['name']} — due: {task['due_date']}")
            elif task and task["status"] == "scheduled":
                recs.append(f"📅 Upcoming task: {task['name']} — scheduled for {task['scheduled_date']}")
        return recs
