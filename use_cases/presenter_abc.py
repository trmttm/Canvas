import abc
from typing import Callable
from typing import List


class PresenterABC(abc.ABC):
    def __init__(self):
        self._observers: List[Callable, ...] = []

    def attach(self, observer: Callable):
        self._observers.append(observer)

    @abc.abstractmethod
    def create_view_model(self, response_model):
        pass

    @abc.abstractmethod
    def present(self, **response_model):
        pass
