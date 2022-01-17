import abc
from typing import Callable
from typing import List


class PresenterABC(abc.ABC):
    def __init__(self):
        self._observers: List[Callable, ...] = []
        self.response_model = {}

    def attach(self, observer: Callable):
        self._observers.append(observer)

    def present(self, shape_id, coordinates_from, coordinates_to, **_):
        self.response_model = {
            'shape_id': shape_id,
            'coordinates_from': coordinates_from,
            'coordinates_to': coordinates_to,
        }
        view_model = self.create_view_model()
        for observer in self._observers:
            observer(view_model)

    @abc.abstractmethod
    def create_view_model(self):
        pass
