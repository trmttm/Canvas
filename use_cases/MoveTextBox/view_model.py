from use_cases.MoveRectangle.view_model import create_view_model as create_view_model_01
from use_cases.MoveText.view_model import create_view_model as create_view_model_02


def create_view_model(response_model):
    sub_response_model_01 = response_model['1']
    sub_response_model_02 = response_model['2']
    return {
        1: create_view_model_01(sub_response_model_01),
        2: create_view_model_02(sub_response_model_02),
    }
