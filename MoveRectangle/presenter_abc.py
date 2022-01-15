import abc
from typing import Callable
from typing import List


class PresenterABC(abc.ABC):
    def __init__(self):
        self._observers: List[Callable, ...] = []
        self.response_model = {}

    def attach(self, observer: Callable):
        self._observers.append(observer)

    def present(self, rectangle_id, delta_x, delta_y):
        self.response_model = {
            'rectangle_id': rectangle_id,
            'delta_x': delta_x,
            'delta_y': delta_y,
        }
        view_model = self.create_view_model()
        for observer in self._observers:
            observer(view_model)

    @abc.abstractmethod
    def create_view_model(self):
        pass
