from dataclasses import dataclass


@dataclass
class Analysis:
    def load_data(self, fname: str):
        with open(fname, 'r') as f:
            self.data = f.readlines()

    def clean_data(self):
        self.data = ...

    def train(self):
        self.model = ...

    def test(self):
        self.test_result = ...

    def print_result(self):
        print(self.test_result)

    def analyze(self, fname: str):
        self.load_data(fname)
        self.clean_data()
        self.train()
        self.test()
        self.print_result()
