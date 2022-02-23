from .use_case import AddTextBox


def controller_command(presenter, entities):
    command = AddTextBox(presenter, entities)
    return command
