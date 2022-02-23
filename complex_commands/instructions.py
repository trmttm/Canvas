import plugin_setting
import request_models as rm


def get_instructions_add_text_box(shape_id, text, fill_color, xy, wh) -> tuple:
    package_names = (plugin_setting.AddRectangle, plugin_setting.SetFillColor, plugin_setting.AddText)
    rectangle_id = f'rectangle_{shape_id}'
    text_id = f'text_{shape_id}'
    request_models = (
        rm.get_request_model_for_add_rectangle(xy, wh, tags=(rectangle_id,)),
        rm.get_request_model_for_set_fill_color(rectangle_id, fill_color),
        rm.get_request_model_for_add_text(xy, text, wh=wh, tags=(text_id,)),
    )
    return package_names, request_models


def get_instruction_move_left(rectangle_id, text_id, delta) -> tuple:
    package_names = (plugin_setting.MoveRectangle, plugin_setting.MoveText)
    request_models = (
        rm.get_request_model_for_move_rectangle(rectangle_id, -delta, 0),
        rm.get_request_model_for_move_text(text_id, -delta, 0),
    )
    return package_names, request_models


def get_instruction_move_right(rectangle_id, text_id, delta) -> tuple:
    package_names = (plugin_setting.MoveRectangle, plugin_setting.MoveText)
    request_models = (
        rm.get_request_model_for_move_rectangle(rectangle_id, delta, 0),
        rm.get_request_model_for_move_text(text_id, delta, 0),
    )
    return package_names, request_models


def get_instruction_move_up(rectangle_id, text_id, delta) -> tuple:
    package_names = (plugin_setting.MoveRectangle, plugin_setting.MoveText)
    request_models = (
        rm.get_request_model_for_move_rectangle(rectangle_id, 0, -delta),
        rm.get_request_model_for_move_text(text_id, 0, -delta),
    )
    return package_names, request_models


def get_instruction_move_down(rectangle_id, text_id, delta) -> tuple:
    package_names = (plugin_setting.MoveRectangle, plugin_setting.MoveText)
    request_models = (
        rm.get_request_model_for_move_rectangle(rectangle_id, 0, delta),
        rm.get_request_model_for_move_text(text_id, 0, delta),
    )
    return package_names, request_models


def get_instructions_remove_all() -> tuple:
    package_names = (plugin_setting.RemoveRectangle, plugin_setting.RemoveText, plugin_setting.RemoveLine)
    request_models = (
        rm.get_request_model_for_remove_rectangle('rectangle_1', ),
        rm.get_request_model_for_remove_text('text_1', ),
        rm.get_request_model_for_remove_line('line_1', ),
    )
    return package_names, request_models
