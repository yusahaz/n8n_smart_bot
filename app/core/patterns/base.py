from abc import ABC, abstractmethod

class PatternDetector(ABC):
    @abstractmethod
    def detect(self, df):
        pass

    @abstractmethod
    def name(self):
        pass
