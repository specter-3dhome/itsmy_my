# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: HomeMaintenance
def edit_record(record_id, field_name, new_value):
    if record_id not in records:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    
    try:
        index = next((i for i, r in enumerate(records) if r['id'] == record_id), -1)
        if field_name in ['rooms', 'tasks', 'workers']:
            records[index][field_name].append(new_value)
        else:
            records[index][field_name] = new_value
        print(f"Запись {record_id} успешно обновлена.")
        return True
    except Exception as e:
        print(f"Ошибка при редактировании: {e}")
        return False
