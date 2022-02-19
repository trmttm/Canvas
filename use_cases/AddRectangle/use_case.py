from typing import Tuple

from ..use_case_abc import UseCaseABC


class AddRectangle(UseCaseABC):
    def configure(self, xy: Tuple[int, int] = (20, 20), wh: Tuple[int, int] = (50, 20), border_color='black',
                  border_width=2, fill='white', tags=(), **_):
        self._response_model = {'xy': xy, 'wh': wh, 'border_color': border_color, 'border_width': border_width,
                                'fill': fill, 'tags': tags}

    def update_entities(self):
        pass

    def present(self):
        self._presenter.present(**self._response_model)
