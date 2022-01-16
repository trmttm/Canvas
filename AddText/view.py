from interface_view import ViewABC


def view_factory(app: ViewABC):
    def view_method(view_model: dict):
        # The following options are not needed when merely adding text
        view_model.update({
            'width': 0,
            'height': 0,
            'text_rotation': 0,
        })
        app.add_text(view_model)

    return view_method
