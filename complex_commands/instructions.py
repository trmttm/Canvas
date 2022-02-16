from use_cases import rm0
from use_cases import rm2
from use_cases import rm5
from use_cases import rm6
from use_cases import rm9


def get_instructions_add_text_box(shape_id, text, fill_color, xy, wh) -> tuple:
    package_numbers = (0, 5, 6)
    request_models = (
        rm0(xy, wh, tags=shape_id),
        rm5(shape_id, fill_color),
        rm6(xy, text, wh, tags=shape_id),
    )
    return package_numbers, request_models


def get_instruction_move_left(shape_id, delta) -> tuple:
    package_numbers = (2, 9)
    request_models = (
        rm2(shape_id, -delta, 0),
        rm9(shape_id, -delta, 0),
    )
    return package_numbers, request_models


def get_instruction_move_right(shape_id, delta) -> tuple:
    package_numbers = (2, 9)
    request_models = (
        rm2(shape_id, delta, 0),
        rm9(shape_id, delta, 0),
    )
    return package_numbers, request_models


def get_instruction_move_up(shape_id, delta) -> tuple:
    package_numbers = (2, 9)
    request_models = (
        rm2(shape_id, 0, -delta),
        rm9(shape_id, 0, -delta),
    )
    return package_numbers, request_models


def get_instruction_move_down(shape_id, delta) -> tuple:
    package_numbers = (2, 9)
    request_models = (
        rm2(shape_id, 0, delta),
        rm9(shape_id, 0, delta),
    )
    return package_numbers, request_models
