import abc


class UseCaseABC(abc.ABC):
    @abc.abstractmethod
    def set_entities(self, entities):
        pass

    @abc.abstractmethod
    def execute(self):
        pass
