# === Stage 20: Добавь восстановление записей из архива ===
# Project: HomeMaintenance
def restore_from_archive(archive_path):
    """Восстанавливает записи из текстового архива."""
    records = []
    with open(archive_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('|||')
            if len(parts) < 4:
                print(f"Пропущена строка без корректного формата: {line}")
                continue
            record_type, fields = parts[0], '|'.join(parts[1:])
            try:
                room_id = int(fields.split('|')[0]) if fields else None
                work_name = fields.split('|')[1] if len(fields.split('|')) > 1 else ''
                executor_name = fields.split('|')[2] if len(fields.split('|')) > 2 else ''
                priority = int(fields.split('|')[3]) if len(fields.split('|')) > 3 else 5
                
                records.append({
                    'type': record_type,
                    'room_id': room_id,
                    'work_name': work_name,
                    'executor_name': executor_name,
                    'priority': priority
                })
            except (ValueError, IndexError):
                print(f"Ошибка парсинга строки: {line}")
    return records
