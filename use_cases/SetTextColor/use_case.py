from use_cases.presenter_abc import PresenterABC
from ..use_case_abc import UseCaseABC


class SetTextColor(UseCaseABC):
    def __init__(self, presenter: PresenterABC, shape_id, color, **_):
        UseCaseABC.__init__(self)

        self._presenter = presenter
        self._shape_id = shape_id
        self._color = color

    def set_entities(self, entities):
        self._entities = entities

    def update_entities(self):
        if self._presenter is None:
            return

        args = self._shape_id, self._color
        self._set_response_model(*args)

    def _set_response_model(self, *args, **kwargs):
        self._response_model = args

    def present(self):
        if self._presenter is None:
            return
        self._presenter.present(*self._response_model)
