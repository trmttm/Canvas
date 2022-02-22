from use_cases.presenter import BasePresenter
from .view_model import create_view_model


def presenter_factory() -> BasePresenter:
    presenter = BasePresenter(create_view_model)
    return presenter
