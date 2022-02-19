import abc

from entities import Entities
from use_cases.presenter_abc import PresenterABC


class UseCaseABC(abc.ABC):
    def __init__(self, presenter: PresenterABC, entities: Entities):
        self._presenter = presenter
        self._entities = entities
        self._response_model = None

    @abc.abstractmethod
    def update_entities(self):
        pass

    @abc.abstractmethod
    def present(self):
        pass

    def execute(self):
        self.update_entities()
        self.present()
