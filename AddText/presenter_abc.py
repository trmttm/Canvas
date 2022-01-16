import abc
from typing import Callable
from typing import List
from typing import Tuple


class PresenterABC(abc.ABC):
    def __init__(self):
        self._observers: List[Callable, ...] = []
        self.response_model = {}

    def attach(self, observer: Callable):
        self._observers.append(observer)

    def present(self, xy: Tuple[int, int], text, tags):
        self.response_model = {
            'x': xy[0],
            'y': xy[1],
            'text': text,
            'tags': tags,
        }
        view_model = self.create_view_model()
        for observer in self._observers:
            observer(view_model)

    @abc.abstractmethod
    def create_view_model(self):
        pass
