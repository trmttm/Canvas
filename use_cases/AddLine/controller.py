from .use_case import AddLine


def controller_command(presenter, entities):
    command = AddLine(presenter, entities)
    return command
