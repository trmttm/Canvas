from .use_case import SetFillColor


def controller_command(presenter, entities):
    command = SetFillColor(presenter, entities)
    return command
