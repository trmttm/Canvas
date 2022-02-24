from interactor import get_shape_types
from ..use_case_abc import UseCaseABC


class SelectShapesInRange(UseCaseABC):
    _group_name = 'selected_shapes'

    def configure(self, rectangle_id, **_):
        shape_ids = []

        x1, y1 = self._entities.rectangles.get_coordinates_from(rectangle_id)
        x2, y2 = self._entities.rectangles.get_coordinates_to(rectangle_id)
        range_coordinates = x1, y1, x2, y2

        for shape_entity in [self._entities.rectangles, self._entities.texts]:
            for shape_id in shape_entity.shape_ids:
                coordinates_from = shape_entity.get_coordinates_from(shape_id)
                coordinates_to = shape_entity.get_coordinates_to(shape_id)
                shape_coordinates = coordinates_from + coordinates_to
                if coordinates_overlap(range_coordinates, shape_coordinates):
                    shape_ids.append(shape_id)

        # Do the same thing for lines, too

        self._configuration = {'group_name': self._group_name, 'contents': shape_ids, }

    def update_entities(self):
        initial_contents = self._entities.group.get_contents(self._group_name)

        self._entities.group.set(**self._configuration)
        self.create_response_model(initial_contents)

    def create_response_model(self, initial_contents: tuple, *args, **kwargs):
        new_contents = self._entities.group.get_contents(self._group_name)
        difference = tuple(set(new_contents) - set(initial_contents))
        shape_types = get_shape_types(self._entities.shape_entities, difference)
        self._response_model = {'group_name': self._group_name, 'contents': difference, 'shape_types': shape_types}


def coordinates_overlap(coords1, coords2) -> bool:
    x11, x12 = min(coords1[0], coords1[2]), max(coords1[0], coords1[2]),
    y11, y12 = min(coords1[1], coords1[3]), max(coords1[1], coords1[3]),
    x21, x22 = min(coords2[0], coords2[2]), max(coords2[0], coords2[2]),
    y21, y22 = min(coords2[1], coords2[3]), max(coords2[1], coords2[3]),

    # If one rectangle is on left side of other
    if x11 >= x22 or x21 >= x12:
        return False

    # If one rectangle is above other
    if y12 <= y21 or y22 <= y11:
        return False

    return True
