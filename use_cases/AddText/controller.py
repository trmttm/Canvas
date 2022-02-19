from .use_case import AddText


def controller_command(presenter, entities):
    command = AddText(presenter, entities)
    return command
