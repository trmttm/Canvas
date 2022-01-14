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

    def present(self, xy: Tuple[int, int], wh: Tuple[int, int], border_color, border_width, fill):
        self.response_model = {
            'x': xy[0],
            'y': xy[1],
            'width': wh[0],
            'height': wh[1],
            'border_color': border_color,
            'border_width': border_width,
            'fill': fill,

        }
        view_model = self.create_view_model()
        for observer in self._observers:
            observer(view_model)

    @abc.abstractmethod
    def create_view_model(self):
        pass


class AddRectangle:
    def __init__(self, presenter: PresenterABC = None, xy: Tuple[int, int] = (20, 20),
                 wh: Tuple[int, int] = (50, 20), border_color='black', border_width=2, fill='white'):
        self._presenter = presenter
        self._x, self._y = xy
        self._width, self._height = wh
        self._border_color = border_color
        self._border_width = border_width
        self._fill = fill

    def execute(self):
        if self._presenter is None:
            return
        args = (self._x, self._y), (self._width, self._height), self._border_color, self._border_width, self._fill
        self._presenter.present(*args)
