from typing import Tuple


def get_request_model(xy: Tuple[int, int] = (20, 20), text: str = 'text', font_size: int = 13,
                      wh: Tuple[int, int] = (0, 0), text_rotation=0, tags=()):
    request_model = {'xy': xy,
                     'text': text,
                     'font_size': font_size,
                     'wh': wh,
                     'text_rotation': text_rotation,
                     'tags': tags, }
    return request_model
