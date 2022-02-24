from .use_case import SetTextValue


def controller_command(presenter, entities):
    command = SetTextValue(presenter, entities)
    return command
