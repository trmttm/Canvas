from .use_case import SetBorderColor


def controller_command(presenter, entities):
    command = SetBorderColor(presenter, entities)
    return command
