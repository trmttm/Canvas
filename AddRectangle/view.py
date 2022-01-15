from interface_view import ViewABC


def view_factory(app: ViewABC):
    def add_rectangle(view_model: dict):
        view_model = {
            'width': view_model.get('width'),
            'height': view_model.get('height'),
            'x': view_model.get('x'),
            'y': view_model.get('y'),
            'border_color': view_model.get('border_color'),
            'border_width': view_model.get('border_width'),
            'fill': view_model.get('fill'),
            'tags': view_model.get('tags'),
        }
        app.add_rectangle(view_model)

    return add_rectangle
