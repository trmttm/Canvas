from use_cases import rm00
from use_cases import rm01
from use_cases import rm02
from use_cases import rm05
from use_cases import rm06
from use_cases import rm09
from use_cases import rm10
from use_cases import rm13


def get_instructions_add_text_box(shape_id, text, fill_color, xy, wh) -> tuple:
    package_numbers = (0, 5, 6)
    request_models = (
        rm00(xy, wh, tags=shape_id),
        rm05(shape_id, fill_color),
        rm06(xy, text, wh, tags=shape_id),
    )
    return package_numbers, request_models


def get_instruction_move_left(shape_id, delta) -> tuple:
    package_numbers = (2, 9)
    request_models = (
        rm02(shape_id, -delta, 0),
        rm09(shape_id, -delta, 0),
    )
    return package_numbers, request_models


def get_instruction_move_right(shape_id, delta) -> tuple:
    package_numbers = (2, 9)
    request_models = (
        rm02(shape_id, delta, 0),
        rm09(shape_id, delta, 0),
    )
    return package_numbers, request_models


def get_instruction_move_up(shape_id, delta) -> tuple:
    package_numbers = (2, 9)
    request_models = (
        rm02(shape_id, 0, -delta),
        rm09(shape_id, 0, -delta),
    )
    return package_numbers, request_models


def get_instruction_move_down(shape_id, delta) -> tuple:
    package_numbers = (2, 9)
    request_models = (
        rm02(shape_id, 0, delta),
        rm09(shape_id, 0, delta),
    )
    return package_numbers, request_models


def get_instructions_remove_all() -> tuple:
    package_numbers = (1, 10, 13)
    request_models = (
        rm01('all', ),
        rm10('all', ),
        rm13('all', ),
    )
    return package_numbers, request_models
