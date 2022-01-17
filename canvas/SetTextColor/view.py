from interface_view import ViewABC


def view_factory(app: ViewABC):
    def view_method(view_model: dict):
        app.set_text_color(view_model)
    return view_method
