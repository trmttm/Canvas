from typing import Tuple

from ..use_case_abc import UseCaseABC


class AddText(UseCaseABC):
    def configure(self, xy: Tuple[int, int] = (20, 20), text: str = 'text', wh: Tuple[int, int] = (0, 0),
                  text_rotation=0, tags=(), **_):
        self._response_model = {'xy': xy,
                                'text': text,
                                'wh': wh,
                                'text_rotation': text_rotation,
                                'tags': tags, }

    def update_entities(self):
        pass

    def present(self):
        self._presenter.present(**self._response_model)
