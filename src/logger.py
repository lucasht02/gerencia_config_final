class Logger:
    def __init__(self, name):
        self.name = name

    def log_info(self, message):
        print(f"[INFO] {self.name}: {message}")

    def log_error(self, message):
        print(f"[ERROR] {self.name}: {message}")