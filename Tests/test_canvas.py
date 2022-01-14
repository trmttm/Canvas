import unittest


def app():
    from view_tkinter import View
    from view_tkinter import tk_interface as intf
    view = View()
    view_model = [
        intf.widget_model('root', 'canvas1', 'canvas', 0, 0, 0, 0, 'nsew', **{'bg': 'light yellow'})
    ]
    view.add_widgets(view_model)
    view.switch_canvas('canvas1')
    return view


def run_app(view):
    view.launch_app()


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
        view = app()

        from UseCases.add_rectangle import AddRectangle
        from UseCases.add_rectangle import PresenterAddRectangleABC

        class PresenterAddRectangle(PresenterAddRectangleABC):
            def create_view_model(self):
                return self.response_model
        presenter = PresenterAddRectangle()
        # presenter.attach(view.add_rectangle)
        
        command = AddRectangle(presenter, (20, 20), (50, 20), border_color='orange', border_width=3, fill='light blue')
        command.execute()

        view_model = [{
            'width': 50,
            'height': 20,
            'x': 20,
            'y': 50,
            'border_color': 'orange',
            'border_width': '2',
            'fill': 'light blue',
            'text': 'hello',
            'text_rotation': 0,
            'tags': '',
        }, ]
        view.add_text_box(view_model)
        run_app(view)


if __name__ == '__main__':
    unittest.main()
