def create_view_model(response_model):
    # items = tuple((shape_id, 'red') for shape_id in response_model.get('contents', ()))
    # view_model = dict(zip(range(len(items)), items))
    shape_ids = response_model.get('contents', ())
    view_model = dict(zip(shape_ids, tuple('red' for _ in shape_ids)))
    return view_model
