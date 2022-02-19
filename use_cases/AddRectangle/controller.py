from .use_case import AddRectangle


def controller_command(presenter, entities):
    command = AddRectangle(presenter, entities)
    return command
