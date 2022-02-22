from use_cases.AddRectangle.use_case import AddRectangle
from use_cases.AddText.use_case import AddText
from ..presenter_abc import PresenterABC
from ..use_case import BaseUseCase


class AddTextBox(BaseUseCase):
    def __init__(self, presenter: PresenterABC, entities):
        BaseUseCase.__init__(self, presenter, entities)
        self._sub_use_cases = [AddRectangle(presenter, entities), AddText(presenter, entities)]

    def configure(self, **request_model):
        for use_case, sub_request_model in zip(self._sub_use_cases, request_model.values()):
            use_case.configure(**sub_request_model)
        self._configuration = request_model

    def update_entities(self):
        for use_case in self._sub_use_cases:
            use_case.update_entities()
