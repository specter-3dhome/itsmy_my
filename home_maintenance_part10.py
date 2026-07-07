# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: HomeMaintenance
def export_state():
    state = {
        "rooms": [r.to_dict() for r in rooms],
        "tasks": [t.to_dict() for t in tasks],
        "workers": [w.to_dict() for w in workers],
        "reminders": [r.to_dict() for r in reminders]
    }
    return json.dumps(state, indent=2)

def export_to_file(filename="home_maintenance.json"):
    state = export_state()
    with open(filename, 'w') as f:
        f.write(state)
    print(f"Exported to {filename}")
