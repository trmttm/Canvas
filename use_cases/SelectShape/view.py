from interface_view import ViewABC


def view_factory(app: ViewABC):
    def view_method(view_model: dict):
        pass  # Do nothing. Be open for higher layer to decide what to present / feedback.

    return view_method
