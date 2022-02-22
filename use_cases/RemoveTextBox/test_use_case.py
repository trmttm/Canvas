import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.RemoveTextBox'
        canvas_color = 'light yellow'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        command = test_app.use_case_command

        # Controller setting
        # Keyboard setting
        from use_cases.AddRectangle.request_model import get_request_model as get_request_model_01
        from use_cases.AddText.request_model import get_request_model as get_request_model_02
        def keyboard_shortcut_handler(modifiers: int, key: str):
            if modifiers == 8 and key == '1':
                wh = (100, 20)
                request_model = {
                    '1': get_request_model_01(view.get_mouse_canvas_coordinate(), wh, 'red', 1, 'light green',
                                              'rect_01'),
                    '2': get_request_model_02(view.get_mouse_canvas_coordinate(), 'New Text!', font_size=13, wh=wh,
                                              tags=('text_01',)),
                }
                command.configure(**request_model)
                command.execute()

        test_app.set_keyboard_shortcut_handler(keyboard_shortcut_handler)

        # Mouse setting
        def upon_mouse_click(request):
            wh = (200, 40)
            request_model = {
                '1': get_request_model_01(view.get_mouse_canvas_coordinate(), wh, 'red', 1, 'light green',
                                          'rect_01'),
                '2': get_request_model_02(view.get_mouse_canvas_coordinate(), 'New Text!', font_size=30, wh=wh,
                                          tags=('text_01',)),
            }
            command.configure(**request_model)
            command.execute()

        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_left_click, {})
        test_app.launch_app()


if __name__ == '__main__':
    unittest.main()
