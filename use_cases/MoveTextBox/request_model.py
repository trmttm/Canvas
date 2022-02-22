from use_cases.MoveRectangle.request_model import get_request_model as get_request_model_01
from use_cases.MoveText.request_model import get_request_model as get_request_model_02


def get_request_model(shape_id_rectangle, shape_id_text, delta_x, delta_y):
    request_model = {
        '1': get_request_model_01(shape_id_rectangle, delta_x, delta_y),
        '2': get_request_model_02(shape_id_text, delta_x, delta_y),
    }
    return request_model
