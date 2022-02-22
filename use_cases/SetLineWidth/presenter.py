from use_cases.presenter import BasePresenter
from use_cases.presenter_abc import PresenterABC
from .view_model import create_view_model


def presenter_factory() -> PresenterABC:
    presenter = BasePresenter(create_view_model)
    return presenter
