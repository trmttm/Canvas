import abc


class UseCaseABC(abc.ABC):
    def __init__(self):
        self._entities = None
        self._response_model = None

    @abc.abstractmethod
    def set_entities(self, entities):
        pass

    @abc.abstractmethod
    def update_entities(self):
        pass

    @abc.abstractmethod
    def present(self):
        pass

    def execute(self):
        self.update_entities()
        self.present()
