from interface_view import ViewABC


def view_factory(app: ViewABC):
    def view_method(view_model: dict):
        app.move_lines(view_model)

    return view_method
