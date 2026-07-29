# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: HomeMaintenance
def print_record(rec):
    if not rec:
        return
    print(f"\n{'═' * 50}")
    print(f"📋 Запись #{rec.id} — {rec.room.name or 'Без помещения'}")
    print(f"   Тип работы : {rec.type}")
    print(f"   Дата       : {rec.date.strftime('%d.%m.%Y') if rec.date else '—'}")
    print(f"   Статус     : {'✅' if rec.done else '⏳'} {rec.status}")
    if rec.person:
        print(f"   Исполнитель: {rec.person.name} ({rec.person.phone})")
    if rec.budget and rec.budget > 0:
        done = f"{rec.budget:.2f}" if rec.done else f"{rec.budget:.2f}/?"
        print(f"   Бюджет     : {done}")
    if rec.notes:
        print(f"   Заметки    : {rec.notes[:60]}{'…' if len(rec.notes) > 60 else ''}")
