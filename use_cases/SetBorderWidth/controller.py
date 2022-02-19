from .use_case import SetBorderWidth


def controller_command(presenter, entities):
    command = SetBorderWidth(presenter, entities)
    return command
