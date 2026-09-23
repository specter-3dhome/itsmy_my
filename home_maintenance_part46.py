# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: HomeMaintenance
class Migration:
    """Движок миграций для HomeMaintenance.
    Позволяет безопасно обновлять структуру данных между версиями проекта,
    не перезаписывая всё с нуля.
    """

    # Текущая версия структуры данных.
    CURRENT_VERSION = 1

    @staticmethod
    def migrate(data: dict) -> dict:
        """Применяет все накопленные миграции к dict data.
        Возвращает обновлённый dict.
        """
        for version, transform in Migration._MIGRATIONS.items():
            if version == Migration.CURRENT_VERSION:
                break
            if version > Migration.CURRENT_VERSION:
                raise RuntimeError(
                    f"Миграция {version} ещё не добавлена. "
                    f"Текущая версия: {Migration.CURRENT_VERSION}"
                )
            data = transform(data)

        Migration.CURRENT_VERSION = max(Migration.CURRENT_VERSION,
                                       max(Migration._MIGRATIONS.keys(), default=0))
        return data

    _MIGRATIONS = {}

    @classmethod
    def register(cls, version: int, transform):
        cls._MIGRATIONS[version] = transform

    @classmethod
    def clear(cls):
        cls._MIGRATIONS.clear()
