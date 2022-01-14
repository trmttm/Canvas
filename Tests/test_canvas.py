import unittest


def run_app(app):
    app.launch_app()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        from UseCases.add_line import AddLine
        from AddRectangle.use_case import AddRectangle
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
        color = {
            1: 'black',
            2: 'red',
            3: 'blue',
            4: 'yellow',
            5: 'orange',
            6: 'pink',
            7: 'purple',
        }

        # Choose App/Main
        from app_tkinter import app_tkinter_factory
        app = app_tkinter_factory()

        # Choose presenter & view
        from AddRectangle.presenter import presenter_add_rectangle_factory
        from AddRectangle.view import view_add_rectangle_factory
        presenter_factory = presenter_add_rectangle_factory
        view_factory = view_add_rectangle_factory

        presenter = presenter_factory()
        view = view_factory(app)
        presenter.attach(view)

        # Define controller command
        from AddRectangle.controller import controller_add_rectangle
        controller_command = controller_add_rectangle

        # Controller setting
        # Keyboard setting
        def keyboard_shortcut_handler(modifiers: int, key: str):
            if modifiers == 8 and key == 'a':
                request_model = {'xy': app.get_mouse_canvas_coordinate(),
                                 'wh': (50, 20),
                                 'border_color': 'red',
                                 'border_width': 1,
                                 'fill': 'light green', }
                controller_command(presenter, request_model)
            elif key in tuple(str(k) for k in range(9)):
                request_model = {'xy': app.get_mouse_canvas_coordinate(),
                                 'wh': (50, 20),
                                 'border_color': color[int(key)],
                                 'border_width': 1,
                                 'fill': 'light green', }
                controller_command(presenter, request_model)

        app.set_keyboard_shortcut_handler('root', keyboard_shortcut_handler)

        # Mouse setting
        from mouse import MouseController
        mouse = MouseController()

        def upon_mouse_click(request):
            request_model = {'xy': (request['x'], request['y']),
                             'wh': (50, 20),
                             'border_color': 'red',
                             'border_width': 1,
                             'fill': 'light green', }
            controller_command(presenter, request_model)

        mouse.configure(0, upon_mouse_click, mouse.is_left_click, {})
        app.bind_command_to_widget('canvas1', mouse.handle)

        run_app(app)


if __name__ == '__main__':
    unittest.main()
