import use_cases


def get_instructions_add_text_box(shape_id, text, fill_color, xy, wh) -> tuple:
    package_numbers = (0, 5, 6)
    rectangle_id = f'rectangle_{shape_id}'
    text_id = f'text_{shape_id}'
    request_models = (
        use_cases.get_request_model_for_add_rectangle(xy, wh, tags=(rectangle_id,)),
        use_cases.get_request_model_for_set_fill_color(rectangle_id, fill_color),
        use_cases.get_request_model_for_add_text(xy, text, wh=wh, tags=(text_id,)),
    )
    return package_numbers, request_models


def get_instruction_move_left(shape_id, delta) -> tuple:
    package_numbers = (2, 9)
    request_models = (
        use_cases.get_request_model_for_move_rectangle(shape_id, -delta, 0),
        use_cases.get_request_model_for_move_text(shape_id, -delta, 0),
    )
    return package_numbers, request_models


def get_instruction_move_right(shape_id, delta) -> tuple:
    package_numbers = (2, 9)
    request_models = (
        use_cases.get_request_model_for_move_rectangle(shape_id, delta, 0),
        use_cases.get_request_model_for_move_text(shape_id, delta, 0),
    )
    return package_numbers, request_models


def get_instruction_move_up(shape_id, delta) -> tuple:
    package_numbers = (2, 9)
    request_models = (
        use_cases.get_request_model_for_move_rectangle(shape_id, 0, -delta),
        use_cases.get_request_model_for_move_text(shape_id, 0, -delta),
    )
    return package_numbers, request_models


def get_instruction_move_down(shape_id, delta) -> tuple:
    package_numbers = (2, 9)
    request_models = (
        use_cases.get_request_model_for_move_rectangle(shape_id, 0, delta),
        use_cases.get_request_model_for_move_text(shape_id, 0, delta),
    )
    return package_numbers, request_models


def get_instructions_remove_all() -> tuple:
    package_numbers = (1, 10, 13)
    request_models = (
        use_cases.get_request_model_for_remove_rectangle('all', ),
        use_cases.get_request_model_for_remove_text('all', ),
        use_cases.get_request_model_for_remove_line('all', ),
    )
    return package_numbers, request_models
