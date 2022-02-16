import abc
from typing import Callable
from typing import List


class PresenterABC(abc.ABC):
    def __init__(self):
        self._observers: List[Callable, ...] = []
        self.response_model = {}

    def attach(self, observer: Callable):
        self._observers.append(observer)

    @abc.abstractmethod
    def present(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def create_view_model(self):
        pass
