from typing import List

from use_cases.AddRectangle.presenter import Presenter as PresenterAddRectangle
from use_cases.AddText.presenter import Presenter as PresenterAddText
from use_cases.presenter_abc import PresenterABC


class Presenter(PresenterABC):
    def __init__(self, ):
        PresenterABC.__init__(self)
        self._presenters: List[PresenterABC] = [PresenterAddRectangle(),PresenterAddText() ]

    def present(self, **response_model):
        for presenter, sub_response_model in zip(self._presenters, response_model.items()):
            presenter.present(**sub_response_model)

    def set_presenter(self, presenter: PresenterABC):
        self._presenters.append(presenter)


def presenter_factory():
    presenter = Presenter()
    return presenter
