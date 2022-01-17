def get_instructions_add_text_box(shape_id, text, fill_color, xy, wh) -> tuple:
    package_numbers = (0, 5, 6)
    request_models = ({'xy': xy, 'wh': wh, 'tags': shape_id},
                      {'shape_id': shape_id, 'color': fill_color},
                      {'xy': xy, 'wh': wh, 'text': text, 'tags': shape_id},
                      )
    return package_numbers, request_models


def get_instruction_move_left(shape_id, delta) -> tuple:
    package_numbers = (2, 9)
    request_models = ({'shape_id': shape_id, 'delta_x': -delta, 'delta_y': 0, },
                      {'shape_id': shape_id, 'delta_x': -delta, 'delta_y': 0, },
                      )
    return package_numbers, request_models


def get_instruction_move_right(shape_id, delta) -> tuple:
    package_numbers = (2, 9)
    request_models = ({'shape_id': shape_id, 'delta_x': delta, 'delta_y': 0, },
                      {'shape_id': shape_id, 'delta_x': delta, 'delta_y': 0, },
                      )
    return package_numbers, request_models


def get_instruction_move_up(shape_id, delta) -> tuple:
    package_numbers = (2, 9)
    request_models = ({'shape_id': shape_id, 'delta_x': 0, 'delta_y': -delta, },
                      {'shape_id': shape_id, 'delta_x': 0, 'delta_y': -delta, },
                      )
    return package_numbers, request_models


def get_instruction_move_down(shape_id, delta) -> tuple:
    package_numbers = (2, 9)
    request_models = ({'shape_id': shape_id, 'delta_x': 0, 'delta_y': delta, },
                      {'shape_id': shape_id, 'delta_x': 0, 'delta_y': delta, },
                      )
    return package_numbers, request_models
