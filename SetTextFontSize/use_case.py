from .presenter_abc import PresenterABC


class SetTextFontSize:
    def __init__(self, presenter: PresenterABC, shape_id, font_size, **_):
        self._presenter = presenter
        self._shape_id = shape_id
        self._font_size = font_size

    def execute(self):
        if self._presenter is None:
            return
        self._presenter.present(self._shape_id, self._font_size)
