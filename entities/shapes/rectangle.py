from entities.shapes.base_shape import ShapesWithXYWH


class Rectangles(ShapesWithXYWH):
    def add(self, xy: tuple = (20, 20), wh: tuple = (50, 20), fill: str = 'white', border_color: str = 'black',
            border_width: int = 1, tags=(), **options):
        options.update({
            'xy': xy,
            'wh': wh,
            'fill': fill,
            'border_color': border_color,
            'border_width': border_width,
            'tags': tags,
        })
        ShapesWithXYWH.add(self, **options)

    def get_fill_color(self, shape_id):
        return self.get(shape_id, 'fill')

    def get_border_width(self, shape_id):
        return self.get(shape_id, 'border_width')

    def set_fill_color(self, shape_id, color):
        self.configure(shape_id, fill=color)

    def set_border_color(self, shape_id, color):
        self.configure(shape_id, border_color=color)

    def set_border_width(self, shape_id, value):
        self.configure(shape_id, border_width=value)
