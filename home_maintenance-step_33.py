# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: HomeMaintenance
class History:
    def __init__(self):
        self._stack = []

    def push(self, state):
        self._stack.append(state)

    def pop(self):
        if not self._stack:
            raise RuntimeError("Nothing to undo")
        return self._stack.pop()

    def can_undo(self):
        return len(self._stack) > 0
