# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: HomeMaintenance
def monthly_stats_for_period(records: list[dict], month: int, year: int) -> dict[str, float]:
    from datetime import date
    total_hours = 0.0
    completed = 0
    for r in records:
        if isinstance(r["date"], str):
            d = date.fromisoformat(r["date"])
        else:
            d = r["date"]
        if d.year == year and d.month == month and r.get("status", "") != "cancelled":
            total_hours += float(r.get("duration", 0) or 0)
            completed += 1
    avg_h = (total_hours / completed) if completed else 0.0
    return {"month": f"{year}-{month:02d}", "completed_jobs": completed, "hours_worked": total_hours, "avg_hours_per_job": round(avg_h, 2)}
