from .use_case import AddRectangle


def controller_add_rectangle(presenter, kwargs):
    command = AddRectangle(presenter, **kwargs)
    command.execute()
