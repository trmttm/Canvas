def add_ten_text_boxes(test_app, view):
    # Add 10 text boxes
    from use_cases.AddTextBox.use_case import AddTextBox
    from use_cases.AddTextBox.presenter import presenter_factory
    from use_cases.AddTextBox.view import view_factory
    from use_cases import get_request_model_for_add_text_box as rm
    presenter = presenter_factory()
    presenter.attach(view_factory(view))
    for i in range(10):
        command_add = AddTextBox(presenter, test_app.entities)
        command_add.configure(**rm(xy_rect=(20, 30 * i), xy_text=(20, 30 * i), text=f'text {i}',
                                   tags_rect=(f'text_box_{i}',), tags_text=(f'text_box_{i}',)))
        command_add.execute()
