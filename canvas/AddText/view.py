from interface_view import ViewABC


def view_factory(app: ViewABC):
    def view_method(view_model: dict):
        # The following options are not needed when merely adding text
        app.add_text(view_model)

    return view_method