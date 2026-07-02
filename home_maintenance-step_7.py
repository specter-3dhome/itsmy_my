# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: HomeMaintenance
from typing import Callable, TypeVar
T = TypeVar('T')

def sort_records(records: list[T], key_func: Callable[[T], any]) -> list[T]:
    """Сортировка списка записей по указанному ключу (дате, приоритету или названию)."""
    return sorted(records, key=key_func)
