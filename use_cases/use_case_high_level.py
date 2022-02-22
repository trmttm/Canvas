from typing import List

from .presenter_abc import PresenterABC
from .use_case_abc import UseCaseABC


class HighLevelUseCase(UseCaseABC):
    def __init__(self, presenter: PresenterABC, entities):
        UseCaseABC.__init__(self, presenter, entities)
        self._sub_use_cases: List[UseCaseABC, ...] = []

    def configure(self, **request_model):
        for use_case, sub_request_model in zip(self._sub_use_cases, request_model.values()):
            use_case.configure(**sub_request_model)
        self._configuration = request_model

    def update_entities(self):
        for use_case in self._sub_use_cases:
            use_case.update_entities()

        self.create_response_model()

    def create_response_model(self, *args, **kwargs):
        self._response_model = self._configuration
