from abc import abstractmethod

from .use_case_abc import UseCaseABC


class BaseUseCase(UseCaseABC):

    @abstractmethod
    def update_entities(self):
        pass

    def present(self):
        self._presenter.present(**self._configuration)

    def execute(self):
        self.update_entities()
        self.present()
