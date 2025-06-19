import json

class ConfigManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.config = {}

    def load(self):
        with open(self.filepath) as f:
            self.config = json.load(f)
        return self.config

    def save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.config, f)