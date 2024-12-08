from abc import ABC, abstractmethod
import random

class Player(ABC):
    @classmethod
    def generate_stat(cls, mean: int, sd: int) -> int: 
        return int(random.gauss(mean, sd)) 
    
    @classmethod
    @abstractmethod
    def stat_metadata(cls) -> dict: 
        pass

    def __init__(self, name: str):
        self.stats = {}
        self.name = name

        for stat, values in self.stat_metadata().items():
            stat_value = self.generate_stat(values["mean"], values["sd"])
            setattr(self, stat, stat_value)
            self.stats[stat] = stat_value