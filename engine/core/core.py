from abc import ABC, abstractmethod
class Core(ABC):
    @abstractmethod
    def start(self, *args, **kwargs):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def render(self, *args, **kwargs):
        pass
