from typing import Tuple


def get_request_model(xy: Tuple[int, int] = (20, 20), wh: Tuple[int, int] = (50, 20), border_color='black',
                      border_width=2, fill='white', tags=()):
    request_model = {'xy': xy,
                     'wh': wh,
                     'border_color': border_color,
                     'border_width': border_width,
                     'fill': fill,
                     'tags': tags}
    return request_model
