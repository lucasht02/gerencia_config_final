class Report:
    def __init__(self, data):
        self.data = data

    def generate(self):
        return f"Report with {len(self.data)} entries"

    def export_csv(self, filepath):
        with open(filepath, 'w') as f:
            f.write(','.join(map(str, self.data)))