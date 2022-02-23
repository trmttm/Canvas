from typing import Iterable

from entities import Shapes


def get_shape_types(shape_entities: Iterable[Shapes], shape_ids):
    shape_types = []
    for shape_id in shape_ids:
        for shape_entity in shape_entities:
            if shape_id in shape_entity:
                shape_types.append(shape_entity.__class__.__name__)
    return tuple(shape_types)
