import abc

from entities import Entities
from use_cases.presenter_abc import PresenterABC


class UseCaseABC(abc.ABC):
    def __init__(self, presenter: PresenterABC, entities: Entities):
        self._presenter = presenter
        self._entities = entities
        self._configuration = None
        self._response_model = None

    @abc.abstractmethod
    def configure(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def update_entities(self):
        pass

    @abc.abstractmethod
    def create_response_model(self, *args, **kwargs):
        pass

    @property
    def response_model(self) -> dict:
        return self._response_model

    def present(self):
        self._presenter.present(**self._response_model)

    def execute(self):
        self.update_entities()
        self.present()
