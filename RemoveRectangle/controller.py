from .use_case import RemoveRectangle


def controller_command(presenter, kwargs):
    command = RemoveRectangle(presenter, **kwargs)
    command.execute()
