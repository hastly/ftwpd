from time import time


class Timer:
    def __init__(self):
        self.start_ts = time()

    def tic(self):
        return f"{self.passed():1.1f}"

    def passed(self):
        return time() - self.start_ts
