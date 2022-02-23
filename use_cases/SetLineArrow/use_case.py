from ..use_case_abc import UseCaseABC


class SetLineArrow(UseCaseABC):
    def configure(self, shape_id, arrow, **_):
        self._configuration = {'shape_id': shape_id, 'arrow': arrow}

    def update_entities(self):
        shape_id_passed = self._configuration.get('shape_id')
        shape_id = self._entities.lines.get_a_single_shape_id_by_tag(shape_id_passed)
        arrow = self._configuration.get('arrow')
        self._entities.lines.set_arrow(shape_id, arrow)
        self.create_response_model()

    def create_response_model(self, *args, **kwargs):
        shape_id_passed = self._configuration.get('shape_id')
        shape_id = self._entities.lines.get_a_single_shape_id_by_tag(shape_id_passed)
        arrow = self._entities.lines.get_arrow(shape_id)
        self._response_model = {'shape_id': shape_id, 'arrow': arrow}
