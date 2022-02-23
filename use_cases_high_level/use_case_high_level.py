from typing import List

from use_cases.presenter_abc import PresenterABC
from use_cases.use_case_abc import UseCaseABC


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
        response_model = {}
        for n, sub_use_case in enumerate(self._sub_use_cases):
            response_model.update({f'{n + 1}': sub_use_case.response_model})
        self._response_model = response_model
