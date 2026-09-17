# === Stage 43: Добавь пагинацию длинных списков ===
# Project: HomeMaintenance
class PaginatedView:
    def __init__(self, items, per_page=10):
        self._items = list(items)
        self._per_page = per_page

    def page(self, page=1):
        start = (page - 1) * self._per_page
        end = start + self._per_page
        return self._items[start:end]

    def total(self):
        return len(self._items)

    def total_pages(self):
        return max(1, (len(self._items) + self._per_page - 1) // self._per_page)
