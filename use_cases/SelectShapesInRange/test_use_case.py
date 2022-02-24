import unittest


class MyTestCase(unittest.TestCase):
    def test_use_case(self):
        from apps.test_app import TestApp
        package_name = 'use_cases.SelectShapesInRange'
        canvas_color = 'white'
        test_app = TestApp(package_name, canvas_color)
        view = test_app.view
        command = test_app.use_case_command

        # Controller setting
        # Keyboard setting
        from request_models import get_request_model_for_select_shape
        get_request_model = get_request_model_for_select_shape

        def keyboard_shortcut_handler(modifiers: int, key: str):
            if modifiers == 8 and key == '1':
                request_model = get_request_model('rectangle_0')
                command.configure(**request_model)
                command.update_entities()
                command.present()

        test_app.set_keyboard_shortcut_handler(keyboard_shortcut_handler)

        # Mouse setting
        def upon_mouse_click(request):
            request_model = get_request_model('rectangle_2')
            command.configure(**request_model)
            command.execute()

        test_app.configure_mouse(upon_mouse_click, test_app.mouse.is_left_click, {})

        from Tests.test_methods import add_ten_text_boxes
        add_ten_text_boxes(test_app, view)

        test_app.launch_app()


if __name__ == '__main__':
    unittest.main()
