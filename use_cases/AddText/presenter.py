from typing import Tuple

from use_cases.presenter_abc import PresenterABC


class Presenter(PresenterABC):
    def present(self, xy: Tuple[int, int], text, width, height, text_rotation, tags, **_):
        self.response_model = {
            'x': xy[0],
            'y': xy[1],
            'text': text,
            'width': width,
            'height': height,
            'text_rotation': text_rotation,
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
