from ..use_case_abc import UseCaseABC


class SetLineArrow(UseCaseABC):
    def configure(self, shape_id, arrow, **_):
        self._configuration = {'shape_id': shape_id, 'arrow': arrow}

    def update_entities(self):
        shape_id = self._configuration.get('shape_id')
        arrow = self._configuration.get('arrow')
        self._entities.lines.set_arrow(shape_id, arrow)

    def present(self):
        self._presenter.present(**self._configuration)
