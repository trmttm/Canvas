import abc
from typing import Callable


class PresenterABC(abc.ABC):
    @abc.abstractmethod
    def attach(self, observer: Callable):
        pass

    @abc.abstractmethod
    def create_view_model(self, response_model):
        pass

    @abc.abstractmethod
    def present(self, **response_model):
        pass
