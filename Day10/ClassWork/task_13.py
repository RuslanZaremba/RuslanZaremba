from abc import ABC, abstractmethod


class Feline(ABC):
    @abstractmethod
    def voice(self):
        raise NotImplemented


class Canine(ABC):
    @abstractmethod
    def voice(self):
        raise NotImplemented
