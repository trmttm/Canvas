from .use_case import RemoveText


def controller_command(presenter, entities):
    command = RemoveText(presenter, entities)
    return command
