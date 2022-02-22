from use_cases.RemoveRectangle.request_model import get_request_model as get_request_model_01
from use_cases.RemoveText.request_model import get_request_model as get_request_model_02


def get_request_model(shape_id_rectangle, shape_id_text):
    request_model = {
        '1': get_request_model_01(shape_id_rectangle),
        '2': get_request_model_02(shape_id_text),
    }
    return request_model
