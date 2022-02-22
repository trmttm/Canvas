def create_view_model(response_model):
    shape_id = response_model.get('shape_id')
    x1, y1 = response_model.get('coordinates_from')
    x2, y2 = response_model.get('coordinates_to')
    view_model = {shape_id: (x1, y1, x2, y2)}
    return view_model
