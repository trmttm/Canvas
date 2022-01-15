from .use_case import MoveRectangle


def controller_command(presenter, kwargs):
    command = MoveRectangle(presenter, **kwargs)
    command.execute()
