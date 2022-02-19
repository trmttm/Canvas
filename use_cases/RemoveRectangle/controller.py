from .use_case import RemoveRectangle


def controller_command(presenter, entities):
    command = RemoveRectangle(presenter, entities)
    return command
