from abc import ABC , abstractmethod
import random
class Joke(ABC):
    def __init__(self,link):
        self._link=link
    @abstractmethod
    def get_random_joke(self):
        pass

