# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: HomeMaintenance
def archive_records(records, cutoff_days=90):
    """Archive records older than `cutoff_days` days."""
    from datetime import date, timedelta
    today = date.today()
    threshold = today - timedelta(days=cutoff_days)
    archived = []
    remaining = []
    for r in records:
        if isinstance(r, dict) and "created_at" in r:
            created = date.fromisoformat(r["created_at"])
            if created < threshold:
                archived.append(r.copy())
                archived[-1]["status"] = "archived"
            else:
                remaining.append(r)
        elif isinstance(r, dict):
            remaining.append(r.copy())
    return archived, remaining
