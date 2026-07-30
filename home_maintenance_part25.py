# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: HomeMaintenance
import datetime


def parse_date(date_str: str) -> datetime.date | None:
    """Парсит дату из строки (DD.MM.YYYY, DD-MM-YYYY, YYYY.MM.DD)."""
    formats = ["%d.%m.%Y", "%d-%m-%Y", "%Y.%m.%d"]
    for fmt in formats:
        try:
            return datetime.date.fromisoformat(date_str.replace("-", "/"))
        except ValueError:
            continue
    raise ValueError(f"Некорректный формат даты: '{date_str}'")


def format_date_display(dt: datetime.date) -> str:
    """Форматирует дату для отображения (например, '25.12.2025')."""
    return dt.strftime("%d.%m.%Y")
