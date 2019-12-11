import diagrams_builder.point as p


class Link:
    x: p.Point
    y: p.Point

    def __init__(self, x: p.Point, y: p.Point):
        self.x = x
        self.y = y
