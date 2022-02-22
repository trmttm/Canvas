def create_view_model(response_model):
    view_model = {response_model.get('shape_id'): (response_model.get('delta_x'), response_model.get('delta_y'))}
    return view_model
