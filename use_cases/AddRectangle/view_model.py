def create_view_model(response_model):
    view_model = {
        'width': response_model.get('wh', (0, 0))[0],
        'height': response_model.get('wh', (0, 0))[1],
        'x': response_model.get('xy', (0, 0))[0],
        'y': response_model.get('xy', (0, 0))[1],
        'border_color': response_model.get('border_color'),
        'border_width': response_model.get('border_width'),
        'fill': response_model.get('fill'),
        'tags': response_model.get('tags'),
    }
    return view_model
