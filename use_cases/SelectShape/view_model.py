def create_view_model(response_model):
    view_model = {
        response_model.get('tags'): {'coordinate_from': response_model.get('xy1'),
                                     'coordinate_to': response_model.get('xy2'),
                                     'line_color': response_model.get('color'),
                                     'line_width': response_model.get('width'),
                                     'tags': response_model.get('tags')}
    }
    return view_model
