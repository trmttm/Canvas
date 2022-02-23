from .use_case import SelectShape


def controller_command(presenter, entities):
    command = SelectShape(presenter, entities)
    return command
