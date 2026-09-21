# === Stage 45: Добавь восстановление из резервной копии ===
# Project: HomeMaintenance
import shutil
import os
from datetime import datetime

def backup_project(source_dir, backup_dir):
    """Создаёт резервную копию проекта HomeMaintenance."""
    if os.path.exists(backup_dir):
        shutil.rmtree(backup_dir)
    shutil.copytree(source_dir, backup_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.rename(backup_dir, f"{backup_dir}_{timestamp}")
    return f"Backup created: {backup_dir}_{timestamp}"

def restore_project(backup_path, target_dir):
    """Восстанавливает проект из резервной копии."""
    if not os.path.exists(backup_path):
        raise FileNotFoundError(f"Backup not found: {backup_path}")
    shutil.copytree(backup_path, target_dir)
    return f"Project restored to: {target_dir}"
