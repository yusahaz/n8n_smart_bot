from abc import ABC, abstractmethod

class IndicatorCalculator(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def calculate(self, df):
        pass
