def create_view_model(response_model):
    view_model = {
        'x': response_model.get('xy', (0, 0))[0],
        'y': response_model.get('xy', (0, 0))[1],
        'text': response_model.get('text'),
        'color': response_model.get('color'),
        'font_size': response_model.get('font_size'),
        'width': response_model.get('wh', (0, 0))[0],
        'height': response_model.get('wh', (0, 0))[1],
        'text_rotation': response_model.get('text_rotation'),
        'tags': response_model.get('tags'),
    }
    return view_model
