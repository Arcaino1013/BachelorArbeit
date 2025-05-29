from abc import ABC, abstractmethod
from typing import List

class AbstractCSVGenerator(ABC):
    @abstractmethod
    def generate_csv(self):
        pass

class CVECSVGenerator(AbstractCSVGenerator):
    def generate_csv(self):
        header_names = ["ID", "Description"]
        pass