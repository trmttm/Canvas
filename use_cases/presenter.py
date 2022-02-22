from typing import Callable
from typing import List

from use_cases.presenter_abc import PresenterABC


class BasePresenter(PresenterABC):
    def __init__(self, create_view_model: Callable = None):
        self._observers: List[Callable, ...] = []
        self._create_view_model = create_view_model

    def attach(self, observer: Callable):
        self._observers.append(observer)

    def present(self, **response_model):
        view_model = self.create_view_model(response_model)
        for observer in self._observers:
            observer(view_model)

    def create_view_model(self, response_model):
        if self._create_view_model is not None:
            return self._create_view_model(response_model)
        else:
            return response_model
