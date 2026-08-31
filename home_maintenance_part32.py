# === Stage 32: Добавь журнал действий пользователя ===
# Project: HomeMaintenance
class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, user: str, action: str, details: str = ""):
        self.entries.append({
            "user": user,
            "action": action,
            "details": details,
            "timestamp": datetime.now().isoformat()
        })

    def get_recent(self, limit: int = 10) -> list:
        return self.entries[-limit:]

    def clear(self):
        self.entries.clear()
