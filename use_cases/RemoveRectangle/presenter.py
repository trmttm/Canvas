from use_cases.presenter_abc import PresenterABC


class Presenter(PresenterABC):
    def present(self, **response_model):
        view_model = response_model
        for observer in self._observers:
            observer(view_model)


def presenter_factory():
    presenter = Presenter()
    return presenter
