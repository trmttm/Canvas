def view_add_rectangle_factory(app):
    def add_rectangle(view_model: dict):
        view_model = [{
            'width': view_model.get('width'),
            'height': view_model.get('height'),
            'x': view_model.get('x'),
            'y': view_model.get('y'),
            'border_color': view_model.get('border_color'),
            'border_width': view_model.get('border_width'),
            'fill': view_model.get('fill'),
            'text': 'hello',
            'text_rotation': 0,
            'tags': '',
        }, ]
        app.add_text_box(view_model)

    return add_rectangle
