from abc import ABC, abstractmethod
import random

class Player(ABC):
    @classmethod
    def generate_stat(cls, mean: int, sd: int) -> int: 
        return random.gauss(mean, sd) 
    
    @classmethod
    @abstractmethod
    def stat_metadata(cls) -> dict: 
        pass

    def __init__(self, name: str):
        self.name = name

        self.stats = {
            stat: self.generate_stat(values["mean"], values["std"])
            for stat, values in self.stat_metadata().items()
        }