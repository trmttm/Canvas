from use_cases.SetBorderColor.view_model import create_view_model as create_view_model_02
from use_cases.SetBorderWidth.view_model import create_view_model as create_view_model_03
from use_cases.SetFillColor.view_model import create_view_model as create_view_model_01
from use_cases.SetTextColor.view_model import create_view_model as create_view_model_04


def create_view_model(response_model):
    sub_response_model_01 = response_model['1']
    sub_response_model_02 = response_model['2']
    sub_response_model_03 = response_model['3']
    sub_response_model_04 = response_model['4']
    return {
        1: create_view_model_01(sub_response_model_01),
        2: create_view_model_02(sub_response_model_02),
        3: create_view_model_03(sub_response_model_03),
        4: create_view_model_04(sub_response_model_04),
    }
