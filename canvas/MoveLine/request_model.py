from typing import Tuple


def get_request_model(shape_id, coordinates_from: Tuple[int, int], coordinates_to: Tuple[int, int]):
    request_model = {'shape_id': shape_id, 'coordinates_from': coordinates_from, 'coordinates_to': coordinates_to}
    return request_model
