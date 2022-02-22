from typing import Tuple

from ..use_case_abc import UseCaseABC


class AddLine(UseCaseABC):

    def configure(self, xy1: Tuple[int, int], xy2: Tuple[int, int], color='black', width=2, arrow_at_start=False,
                  arrow_at_end=False, tags=(), **_):
        arrow = None
        if arrow_at_start and arrow_at_end:
            arrow = 'both'
        elif arrow_at_start:
            arrow = 'start'
        elif arrow_at_end:
            arrow = 'end'
        self._configuration = {
            'xy1': xy1,
            'xy2': xy2,
            'color': color,
            'width': width,
            'tags': tags,
            'arrow': arrow, }

    def update_entities(self):
        shape_id = self._entities.lines.add(**self._configuration)
        self.create_response_model(shape_id)

    def create_response_model(self, shape_id, *args, **kwargs):
        self._response_model = self._entities.lines.get_configuration(shape_id)
