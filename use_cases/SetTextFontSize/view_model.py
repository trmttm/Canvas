def create_view_model(response_model):
    view_model = {response_model.get('shape_id'): response_model.get('font_size')}
    return view_model
