# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: HomeMaintenance
def search_records(records, query):
    """Search records by multiple fields case-insensitively."""
    query = query.lower()
    results = []
    for record in records:
        if any(query in str(getattr(record, field, '')).lower() for field in ('name', 'room_name', 'description')):
            results.append(record)
    return results
