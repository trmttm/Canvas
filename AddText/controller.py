from .use_case import AddText


def controller_command(presenter, kwargs):
    command = AddText(presenter, **kwargs)
    command.execute()
