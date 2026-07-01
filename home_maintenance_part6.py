# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: HomeMaintenance
from typing import Callable, Optional
def filter_records(records: list[dict], status: Optional[str] = None, category: Optional[str] = None, tags: Optional[list[str]] = None) -> list[dict]:
    if not records: return []
    filtered = [r for r in records if (not status or r.get('status') == status) and (not category or r.get('category') == category)]
    if tags is not None:
        def has_any_tag(rec):
            rec_tags = rec.get('tags', [])
            return any(t.lower() in [tag.lower() for tag in rec_tags] for t in tags)
        filtered = [r for r in filtered if has_any_tag(r)]
    return filtered

def get_filtered_by_status(records: list[dict], status: str) -> list[dict]:
    return filter_records(records, status=status)

def get_filtered_by_category(records: list[dict], category: str) -> list[dict]:
    return filter_records(records, category=category)

def get_filtered_by_tags(records: list[dict], tags: list[str]) -> list[dict]:
    return filter_records(records, tags=tags)
