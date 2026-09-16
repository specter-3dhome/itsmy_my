# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: HomeMaintenance
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    @staticmethod
    def enabled():
        try:
            import os
            return os.name != "nt"
        except Exception:
            return True

    @staticmethod
    def disable():
        import sys
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

    @staticmethod
    def enable():
        import sys
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

    @staticmethod
    def print(text="", color=None, bold=False):
        if Color.enabled():
            if color:
                text = f"{color}{text}{Color.RESET}"
            if bold:
                text = f"{Color.BOLD}{text}{Color.RESET}"
            print(text)
        else:
            print(text)
