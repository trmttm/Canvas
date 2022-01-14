from interface_view import ViewABC


def view_factory(app: ViewABC):
    def add_rectangle(view_model: dict):
        view_model = [view_model['rectangle_id']]
        app.remove_text_box(view_model)

    return add_rectangle
