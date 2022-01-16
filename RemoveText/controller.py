from .use_case import RemoveText


def controller_command(presenter, kwargs):
    command = RemoveText(presenter, **kwargs)
    return command
