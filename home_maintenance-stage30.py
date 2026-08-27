# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: HomeMaintenance
class UserProfile:
    def __init__(self, username, role="user"):
        self.username = username
        self.role = role

    def __repr__(self):
        return f"UserProfile({self.username!r}, {self.role!r})"

class ProfileManager:
    def __init__(self):
        self._profiles = {}

    def register(self, profile: UserProfile):
        self._profiles[profile.username] = profile

    def get(self, username):
        return self._profiles.get(username)

    def list(self):
        return list(self._profiles.values())
