# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: HomeMaintenance
def delete_record(table_name, record_id):
    if table_name not in db:
        raise ValueError(f"Таблица {table_name} не найдена")
    if record_id not in db[table_name]:
        print(f"Запись с ID {record_id} в таблице {table_name} отсутствует")
        return False
    del db[table_name][record_id]
    print(f"Удаление записи {record_id} из таблицы {table_name} завершено")
    return True

def handle_missing_ids():
    for table in list(db.keys()):
        if not isinstance(db[table], dict):
            continue
        invalid_keys = [k for k, v in db[table].items() if not isinstance(k, int)]
        if invalid_keys:
            print(f"В таблице {table} найдены некорректные ID: {invalid_keys}")
