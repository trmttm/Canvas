from ..use_case_abc import UseCaseABC


class RemoveRectangle(UseCaseABC):
    def configure(self, shape_id, **_):
        self._configuration = {'shape_id': shape_id}

    def update_entities(self):
        shape_id_passed = self._configuration.get('shape_id')
        shape_id = self._entities.rectangles.get_a_single_shape_id_by_tag(shape_id_passed)
        self._entities.rectangles.remove(shape_id)
        self.create_response_model(shape_id)

    def create_response_model(self, shape_id, *args, **kwargs):
        self._response_model = {'shape_id': shape_id}
