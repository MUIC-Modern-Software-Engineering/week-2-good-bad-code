from dataclasses import dataclass

Data = List[int]
Model = int
class DataLoader:
    def load_data(self)-> Data:
        ...

class DataCleaner:
    def clean_data(self, data: Data) -> Data:
        ...

class ModelTrainer:
    def train_model(self, data: Data) -> Model:
        ...

class ModelTester:
    def test_model(self, model: Model, data: Data) -> TestResult:
        ...

class TestResultPrinter:
    def print_test_result(self, test_result: TestResult):
        ...


@dataclass
class Analysis:
    data_loader: DataLoader
    data_cleaner: DataCleaner
    model_trainer: ModelTrainer
    model_tester: ModelTester
    test_result_printer: TestResultPrinter

    def analyze(self, fname: str):
        data = self.data_loader.load_data(fname)
        clean_data = self.data_cleaner.clean_data()
        model = self.model_trainer.train()
        test_result = self.model_tester.test(model)
        self.test_result_printer.print_test_result(test_result)

    @classmethod
    def default_analysis(cls) -> Analysis:
        ...
