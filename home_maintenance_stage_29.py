# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: HomeMaintenance
_config = {
    "app_name": "HomeMaintenance",
    "version": "0.29",
    "language": "ru",
    "default_room": "living_room",
    "default_worker": "maintenance_team",
    "notifications": {
        "enabled": True,
        "method": "print",
        "quiet_hours": (22, 7),
        "reminder_days": [1, 3, 7],
    },
    "logging": {
        "level": "INFO",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    },
}
