from request_models import get_request_model_for_set_border_color
from request_models import get_request_model_for_set_border_width
from request_models import get_request_model_for_set_fill_color
from request_models import get_request_model_for_set_text_color


def get_request_model(rectangle_id, color_fill, color_border, width_border, text_id, color_text):
    request_model = {
        '1': get_request_model_for_set_fill_color(rectangle_id, color_fill),
        '2': get_request_model_for_set_border_color(rectangle_id, color_border),
        '3': get_request_model_for_set_border_width(rectangle_id, width_border),
        '4': get_request_model_for_set_text_color(text_id, color_text),
    }
    return request_model
