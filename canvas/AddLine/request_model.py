from typing import Tuple


def get_request_model(xy1: Tuple[int, int], xy2: Tuple[int, int], color='black', width=2, arrow_at_start=False,
                      arrow_at_end=False, tags=()):
    request_model = {'xy1': xy1,
                     'xy2': xy2,
                     'width': width,
                     'color': color,
                     'arrow_at_start': arrow_at_start,
                     'arrow_at_end': arrow_at_end,
                     'tags': tags,
                     }
    return request_model
