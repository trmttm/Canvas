from app import App
from entities import Entities


class AddNewTextBox:

    def __init__(self, app: App, entities: Entities, text: str = 'Text', fill_color='white', xy: tuple = (10, 10),
                 wh: tuple = (100, 20)):
        self._app = app
        self._entities = entities

        self._options = {'text': text, 'fill_color': fill_color, 'xy': xy, 'wh': wh}
        self._commands = ()

    def configure(self, **options):
        self._options.update(options)

    def update_entities(self):
        from complex_commands import instructions as i

        new_shape_id = self._entities.shapes.add_text_box(**self._options)
        self._entities.selection.select(new_shape_id)
        xy = self._options['xy']
        self.configure(xy=(xy[0], xy[1] + 20))
        instruction = i.get_instructions_add_text_box(new_shape_id, **self._options)
        self._commands = self._app.create_commands(*instruction)
        self._app.update_entities(self._commands)

    def present(self):
        self._app.present(self._commands)

    def execute(self):
        self.update_entities()
        self.present()
