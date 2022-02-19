from .use_case import MoveRectangle


def controller_command(presenter, entities):
    command = MoveRectangle(presenter, entities)
    return command
