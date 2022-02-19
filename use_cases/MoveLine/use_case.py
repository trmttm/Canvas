from ..use_case_abc import UseCaseABC


class MoveLine(UseCaseABC):
    def configure(self, shape_id, coordinates_from, coordinates_to, **_):
        self._response_model = {'shape_id': shape_id, 'coordinates_from': coordinates_from,
                                'coordinates_to': coordinates_to}

    def update_entities(self):
        pass

    def present(self):
        self._presenter.present(**self._response_model)
