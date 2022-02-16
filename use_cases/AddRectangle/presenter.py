from typing import Tuple

from use_cases.presenter_abc import PresenterABC


class Presenter(PresenterABC):
    def present(self, xy: Tuple[int, int], wh: Tuple[int, int], border_color, border_width, fill, tags, **_):
        self.response_model = {
            'x': xy[0],
            'y': xy[1],
            'width': wh[0],
            'height': wh[1],
            'border_color': border_color,
            'border_width': border_width,
            'fill': fill,
            'tags': tags,

        }
        view_model = self.create_view_model()
        for observer in self._observers:
            observer(view_model)

    def create_view_model(self):
        return self.response_model


def presenter_factory():
    presenter = Presenter()
    return presenter
