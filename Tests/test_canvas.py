import unittest


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


if __name__ == '__main__':
    unittest.main()
