# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: HomeMaintenance
TEMPLATES = {
    "cleaning": {
        "title": "Уборка",
        "description": "Регулярная уборка помещения",
        "default_duration": 2,
        "default_cost": 500,
        "default_skill": "general",
    },
    "painting": {
        "title": "Покраска",
        "description": "Покраска стен или потолков",
        "default_duration": 4,
        "default_cost": 1500,
        "default_skill": "painter",
    },
    "plumbing": {
        "title": "Сантехника",
        "description": "Ремонт или замена сантехнических элементов",
        "default_duration": 3,
        "default_cost": 2000,
        "default_skill": "plumber",
    },
    "electrical": {
        "title": "Электрика",
        "description": "Ремонт или замена электрических элементов",
        "default_duration": 2,
        "default_cost": 1500,
        "default_skill": "electrician",
    },
    "general_repair": {
        "title": "Общий ремонт",
        "description": "Различные мелкие ремонтные работы",
        "default_duration": 1,
        "default_cost": 500,
        "default_skill": "general",
    },
}
