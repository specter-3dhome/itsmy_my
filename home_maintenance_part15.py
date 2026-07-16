# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: HomeMaintenance
def weekly_stats(self):
    """Generate per-date weekly statistics for all tasks."""
    stats = {}
    today = self.current_date
    for w in range(7):
        d = today - timedelta(days=w)
        key = str(d.date())
        if key not in stats:
            stats[key] = {"planned": 0, "done": 0, "failed": 0}
        for task in self.tasks.values():
            if str(task['date']).split(' ')[-1].replace('-', '') == key.split('-')[-1]:
                continue
            if str(task['date'])[:10] == key:
                stats[key][task['status']] = stats[key].get(task['status'], 0) + 1
    return stats
