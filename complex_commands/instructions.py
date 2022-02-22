import use_cases


def get_instructions_add_text_box(shape_id, text, fill_color, xy, wh) -> tuple:
    package_names = (use_cases.AddRectangle, use_cases.SetFillColor, use_cases.AddText)
    rectangle_id = f'rectangle_{shape_id}'
    text_id = f'text_{shape_id}'
    request_models = (
        use_cases.get_request_model_for_add_rectangle(xy, wh, tags=(rectangle_id,)),
        use_cases.get_request_model_for_set_fill_color(rectangle_id, fill_color),
        use_cases.get_request_model_for_add_text(xy, text, wh=wh, tags=(text_id,)),
    )
    return package_names, request_models


def get_instruction_move_left(shape_id, delta) -> tuple:
    package_names = (use_cases.MoveRectangle, use_cases.MoveText)
    request_models = (
        use_cases.get_request_model_for_move_rectangle(shape_id, -delta, 0),
        use_cases.get_request_model_for_move_text(shape_id, -delta, 0),
    )
    return package_names, request_models


def get_instruction_move_right(shape_id, delta) -> tuple:
    package_names = (use_cases.MoveRectangle, use_cases.MoveText)
    request_models = (
        use_cases.get_request_model_for_move_rectangle(shape_id, delta, 0),
        use_cases.get_request_model_for_move_text(shape_id, delta, 0),
    )
    return package_names, request_models


def get_instruction_move_up(shape_id, delta) -> tuple:
    package_names = (use_cases.MoveRectangle, use_cases.MoveText)
    request_models = (
        use_cases.get_request_model_for_move_rectangle(shape_id, 0, -delta),
        use_cases.get_request_model_for_move_text(shape_id, 0, -delta),
    )
    return package_names, request_models


def get_instruction_move_down(shape_id, delta) -> tuple:
    package_names = (use_cases.MoveRectangle, use_cases.MoveText)
    request_models = (
        use_cases.get_request_model_for_move_rectangle(shape_id, 0, delta),
        use_cases.get_request_model_for_move_text(shape_id, 0, delta),
    )
    return package_names, request_models


def get_instructions_remove_all() -> tuple:
    package_names = (use_cases.RemoveRectangle, use_cases.RemoveText, use_cases.RemoveLine)
    request_models = (
        use_cases.get_request_model_for_remove_rectangle('all', ),
        use_cases.get_request_model_for_remove_text('all', ),
        use_cases.get_request_model_for_remove_line('all', ),
    )
    return package_names, request_models
