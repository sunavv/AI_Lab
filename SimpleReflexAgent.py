class SimpleReflexAgent:
    def __init__(self):
        self.location = 'A'
        self.status = {'A': 'dirty', 'B': 'dirty'}

    def move_and_clean(self):
        if self.status[self.location] == 'dirty':
            print(f"Cleaning {self.location}")
            self.status[self.location] = 'clean'
        else:
            self.location = 'B' if self.location == 'A' else 'A'
        print(f"Moving to {self.location}")

agent = SimpleReflexAgent()
for _ in range(4):
    agent.move_and_clean()
