# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: HomeMaintenance
def switch_profile():
    """Переключение активного пользовательского профиля."""
    if not hasattr(switch_profile, '_profiles'):
        switch_profile._profiles = {}
    if not hasattr(switch_profile, '_active'):
        switch_profile._active = None
    print("Доступные профили:", list(switch_profile._profiles.keys()))
    name = input("Введите имя профиля для переключения: ")
    if name in switch_profile._profiles:
        switch_profile._active = name
        print(f"Переключен на профиль: {name}")
    else:
        print(f"Профиль '{name}' не найден")
