def create_view_model(response_model):
    view_model = {response_model['shape_id']: response_model['width']}
    return view_model