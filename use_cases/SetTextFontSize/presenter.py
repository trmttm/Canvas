from use_cases.presenter import BasePresenter
from .view_model import create_view_model


class Presenter(BasePresenter):
    def create_view_model(self, response_model):
        return create_view_model(response_model)


def presenter_factory():
    presenter = Presenter()
    return presenter
