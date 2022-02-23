from interactor import get_shape_types
from ..use_case_abc import UseCaseABC


class SelectShape(UseCaseABC):
    _group_name = 'selected_shapes'

    def configure(self, shape_id, **_):
        self._configuration = {'group_name': self._group_name, 'content': shape_id, }

    def update_entities(self):
        initial_contents = self._entities.group.get_contents(self._group_name)

        self._entities.group.add(**self._configuration)
        self.create_response_model(initial_contents)

    def create_response_model(self, initial_contents: tuple, *args, **kwargs):
        new_contents = self._entities.group.get_contents(self._group_name)
        difference = tuple(set(new_contents) - set(initial_contents))
        shape_types = get_shape_types(self._entities.shape_entities, difference)
        self._response_model = {'group_name': self._group_name, 'contents': difference, 'shape_types': shape_types}
