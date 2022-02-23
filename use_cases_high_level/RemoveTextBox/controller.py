from .use_case import RemoveTextBox


def controller_command(presenter, entities):
    command = RemoveTextBox(presenter, entities)
    return command
