from typing import Tuple

from ..use_case_abc import UseCaseABC


class AddRectangle(UseCaseABC):
    def configure(self, xy: Tuple[int, int] = (20, 20), wh: Tuple[int, int] = (50, 20), border_color='black',
                  border_width=2, fill='white', tags=(), **_):
        self._configuration = {
            'xy': xy,
            'wh': wh,
            'border_color': border_color,
            'border_width': border_width,
            'fill': fill,
            'tags': tags,
        }

    def update_entities(self):
        rm = self._configuration
        self._entities.rectangles.add(
            rm['xy'],
            rm['wh'],
            rm['fill'],
            rm['border_color'],
            rm['border_width'],
            rm['tags'],
        )

    def present(self):
        self._presenter.present(**self._configuration)
