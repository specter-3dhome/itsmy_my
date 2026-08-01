# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: HomeMaintenance
def demo():
    print("=== HomeMaintenance Demo ===")
    print(f"Помещения: {len(buildings)}")
    for b in buildings:
        print(f"  - {b.name}: {len(b.rooms) if hasattr(b, 'rooms') else 0} комнат")

print(demo())
