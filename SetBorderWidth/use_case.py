from .presenter_abc import PresenterABC


class SetBorderWidth:
    def __init__(self, presenter: PresenterABC, shape_id, width, **_):
        self._presenter = presenter
        self._shape_id = shape_id
        self._width = width

    def execute(self):
        if self._presenter is None:
            return
        self._presenter.present(self._shape_id, self._width)
