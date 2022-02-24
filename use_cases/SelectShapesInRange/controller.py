from .use_case import SelectShapesInRange


def controller_command(presenter, entities):
    command = SelectShapesInRange(presenter, entities)
    return command
