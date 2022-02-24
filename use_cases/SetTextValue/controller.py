from .use_case import SetTextColor


def controller_command(presenter, entities):
    command = SetTextColor(presenter, entities)
    return command
