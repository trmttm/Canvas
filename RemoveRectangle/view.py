from interface_view import ViewABC


def view_factory(app: ViewABC):
    def add_rectangle(view_model: dict):
        app.remove_text_box([view_model['rectangle_id']])
    return add_rectangle
