from abc import ABC, abstractmethod, abstractproperty
class Component(ABC):
    @abstractmethod
    def __init__(self):
        self._package = None

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def update(self, package = None):
        pass

    def empty(self):
        if self._package:
            return False
        return True

    def set_display(self, display):
        pass

