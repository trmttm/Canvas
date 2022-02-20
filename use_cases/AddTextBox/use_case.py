from use_cases.AddRectangle.use_case import AddRectangle
from use_cases.AddText.use_case import AddText
from ..presenter_abc import PresenterABC
from ..use_case_abc import UseCaseABC


class AddTextBox(UseCaseABC):
    def __init__(self, presenter: PresenterABC, entities):
        UseCaseABC.__init__(self, presenter, entities)
        self._sub_use_cases = [AddRectangle(presenter, entities), AddText(presenter, entities)]

    def configure(self, **request_model):
        for use_case, sub_request_model in zip(self._sub_use_cases, request_model.values()):
            use_case.configure(**sub_request_model)
        self._response_model = request_model

    def update_entities(self):
        for use_case in self._sub_use_cases:
            use_case.update_entities()

    def present(self):
        self._presenter.present(**self._response_model)
