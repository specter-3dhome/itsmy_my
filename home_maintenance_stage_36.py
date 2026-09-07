# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: HomeMaintenance
def repair_simple_issues(data):
    """Check data integrity and fix common simple problems."""
    if not isinstance(data, dict):
        return {"error": "Data must be a dictionary", "status": "corrupted"}
    
    if "rooms" not in data:
        data["rooms"] = []
    if "tasks" not in data:
        data["tasks"] = []
    if "workers" not in data:
        data["workers"] = []
    if "reminders" not in data:
        data["reminders"] = []
    
    if not isinstance(data["rooms"], list):
        data["rooms"] = []
    if not isinstance(data["tasks"], list):
        data["tasks"] = []
    if not isinstance(data["workers"], list):
        data["workers"] = []
    if not isinstance(data["reminders"], list):
        data["reminders"] = []
    
    return {"status": "repaired", "details": "Data structure validated and normalized"}
