from typing import Tuple

from use_cases.presenter_abc import PresenterABC


class Presenter(PresenterABC):
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

    def create_view_model(self):
        view_model = {
            self.response_model['tags']: self.response_model,
        }
        return view_model


def presenter_factory():
    presenter = Presenter()
    return presenter
