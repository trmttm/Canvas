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

    def present(self, xy1: Tuple[int, int], xy2: Tuple[int, int], color, width, tags, arrow, **_):
        self.response_model = {
            'coordinate_from': xy1,
            'coordinate_to': xy2,
            'line_color': color,
            'line_width': width,
            'tags': tags,
            'arrow': arrow,

        }
        view_model = self.create_view_model()
        for observer in self._observers:
            observer(view_model)

    @abc.abstractmethod
    def create_view_model(self):
        pass
