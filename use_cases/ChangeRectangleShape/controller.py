from .use_case import ChangeRectangleShape


def controller_command(presenter, entities):
    command = ChangeRectangleShape(presenter, entities)
    return command
