from interface_view import ViewABC


def view_factory(app: ViewABC):
    def view_method(view_model: dict):
        app.remove_shape([view_model['shape_id']])

    return view_method
