from .presenter_abc import PresenterABC

from ..use_case_abc import UseCaseABC


class SetLineArrow(UseCaseABC):
    def __init__(self, presenter: PresenterABC, shape_id, arrow, **_):
        """

        :param presenter:
        :param shape_id:
        :param arrow: 'start', 'end', 'both', or None
        :param _:
        """
        self._presenter = presenter
        self._shape_id = shape_id
        self._arrow = arrow

    def set_entities(self, entities):
        self._entities = entities

    def update_entities(self):
        if self._presenter is None:
            return

        args = self._shape_id, self._arrow
        self._update_entities(*args)
        self._presenter.present(*args)

    def _update_entities(self, *args, **kwargs):
        pass
