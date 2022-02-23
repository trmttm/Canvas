from typing import Tuple

import request_models as rm


def get_request_model(xy_rect: Tuple[int, int] = (20, 20), wh_rect: Tuple[int, int] = (50, 20), border_color='black',
                      border_width=2, fill='white', tags_rect=(), xy_text=(20, 20), text='text', text_color='black',
                      font_size: int = 13, wh_text=(50, 20), text_rotation=0, tags_text=()):
    request_model = {
        '1': rm.get_request_model_for_add_rectangle(xy_rect, wh_rect, border_color, border_width, fill, tags_rect),
        '2': rm.get_request_model_for_add_text(xy_text, text, text_color, font_size, wh_text, text_rotation, tags_text),
    }
    return request_model
