# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: HomeMaintenance
def print_table(rows, headers):
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, v in enumerate(row):
            if len(str(v)) > col_widths[i]:
                col_widths[i] = len(str(v))

    header_line = ' | '.join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers))
    separator = '-+-'.join('-' * w for w in col_widths)

    print(header_line)
    print(separator)
    for row in rows:
        line = ' | '.join(str(v).ljust(col_widths[i]) for i, v in enumerate(row))
        print(line)


if __name__ == '__main__':
    rooms = ['Кухня', 'Спальня', 'Гостиная']
    tasks = ['Мыть полы', 'Пылесосить', 'Убрать мусор']

    data = list(zip(rooms, tasks))
    headers = ['Помещение', 'Работа']
    print_table(data, headers)
