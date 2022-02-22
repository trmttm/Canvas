from abc import abstractmethod

from .presenter_abc import PresenterABC


class BasePresenter(PresenterABC):
    def present(self, **response_model):
        view_model = self.create_view_model(response_model)
        for observer in self._observers:
            observer(view_model)

    @abstractmethod
    def create_view_model(self, response_model):
        pass
