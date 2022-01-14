import unittest


def main():
    from view_tkinter import View
    from view_tkinter import tk_interface as intf
    view = View()
    view_model = [
        intf.widget_model('root', 'canvas1', 'canvas', 0, 0, 0, 0, 'nsew', **{'bg': 'light yellow'})
    ]
    view.add_widgets(view_model)
    view.switch_canvas('canvas1')
    return view


def presenter_add_rectangle_factory():
    from UseCases.add_rectangle import PresenterAddRectangleABC
    class PresenterAddRectangle(PresenterAddRectangleABC):
        def create_view_model(self):
            return self.response_model

    presenter = PresenterAddRectangle()
    return presenter


def run_app(app):
    app.launch_app()


def view_add_rectangle_factory(app):
    def add_rectangle(view_model: dict):
        view_model = [{
            'width': view_model.get('width'),
            'height': view_model.get('height'),
            'x': view_model.get('x'),
            'y': view_model.get('y'),
            'border_color': view_model.get('border_color'),
            'border_width': view_model.get('border_width'),
            'fill': view_model.get('fill'),
            'text': 'hello',
            'text_rotation': 0,
            'tags': '',
        }, ]
        app.add_text_box(view_model)

    return add_rectangle


def controller_add_rectangle(presenter, kwargs):
    from UseCases.add_rectangle import AddRectangle
    command = AddRectangle(presenter, **kwargs)
    command.execute()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        from UseCases.add_line import AddLine
        from UseCases.add_rectangle import AddRectangle
        from UseCases.add_text import AddText
        from UseCases.change_font import ChangeFont
        from UseCases.change_font_size import ChangeFontSize
        from UseCases.change_text_color import ChangeTextColor
        from UseCases.move_line import MoveLine
        from UseCases.move_rectangle import MoveRectangle
        from UseCases.move_text import MoveText
        from UseCases.remove_line import RemoveLine
        from UseCases.remove_rectangle import RemoveRectangle
        from UseCases.remove_text import RemoveText
        from UseCases.set_arrow_head import SetArrowHead
        from UseCases.set_border_color import SetBorderColor
        from UseCases.set_border_width import SetBorderWidth
        from UseCases.set_fill_color import SetFillColor
        from UseCases.set_line_color import SetLineColor
        from UseCases.set_line_width import SetLineWidth

        add_rectangle = AddRectangle()
        remove_rectangle = RemoveRectangle()
        move_rectangle = MoveRectangle()
        set_border_width = SetBorderWidth()
        set_border_color = SetBorderColor()
        set_fill_color = SetFillColor()

        add_text = AddText()
        remove_text = RemoveText()
        move_text = MoveText()
        change_font = ChangeFont()
        change_font_size = ChangeFontSize()
        change_text_color = ChangeTextColor()

        add_line = AddLine()
        remove_line = RemoveLine()
        move_line = MoveLine()
        set_arrow_head = SetArrowHead()
        set_line_width = SetLineWidth()
        set_line_color = SetLineColor()

    def test_add_rectangle(self):
        app = main()

        # Set up AddRectangle elements
        presenter = presenter_add_rectangle_factory()
        view = view_add_rectangle_factory(app)
        presenter.attach(view)

        # Controller setting
        # Keyboard
        def keyboard_shortcut_handler(modifiers: int, key: str):
            if modifiers == 8 and key == 'a':
                request_model = {'xy': app.get_mouse_canvas_coordinate(),
                                 'wh': (50, 20),
                                 'border_color': 'red',
                                 'border_width': 1,
                                 'fill': 'light green', }
                controller_add_rectangle(presenter, request_model)

        app.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

        # Mouse
        from mouse import MouseController
        mouse = MouseController()

        def upon_mouse_click(request):
            request_model = {'xy': (request['x'], request['y']),
                             'wh': (50, 20),
                             'border_color': 'red',
                             'border_width': 1,
                             'fill': 'light green', }
            controller_add_rectangle(presenter, request_model)

        mouse.configure(0, upon_mouse_click, mouse.is_left_click, {})
        app.bind_command_to_widget('canvas1', mouse.handle)

        request_model = {'xy': (20, 20),
                         'wh': (50, 20),
                         'border_color': 'red',
                         'border_width': 1,
                         'fill': 'light green', }
        controller_add_rectangle(presenter, request_model)

        run_app(app)


if __name__ == '__main__':
    unittest.main()
