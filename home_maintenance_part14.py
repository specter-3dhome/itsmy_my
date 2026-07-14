# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: HomeMaintenance
def generate_summary():
    print("=" * 40)
    print("🏠 СВОДКА ПО СТАНУ ХОЗЯЙСТВА")
    print("=" * 40)
    
    total_rooms = len(rooms)
    completed_works = sum(1 for w in works if w.status == "completed")
    active_workers = set()
    
    for room in rooms:
        for work in room.works:
            if work.status != "completed":
                active_workers.add(work.worker_name)
    
    print(f"📊 Комнат: {total_rooms}")
    print(f"✅ Завершённых работ: {completed_works} из {len(works)}")
    print(f"⏳ Активных исполнителей: {len(active_workers)}")
    
    if reminders:
        urgent = [r for r in reminders if r.priority == "high"]
        print(f"🔴 Срочных напоминаний: {len(urgent)}")
        for r in urgent:
            print(f"   → [{r.target}] {r.message}")
    
    print("=" * 40)
