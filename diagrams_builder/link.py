from diagrams_builder.points import Point


class Link:
    x: Point
    y: Point

    def __init__(self, x: Point, y: Point):
        self.x = x
        self.y = y

    def __repr__(self):
        return "{} -> {}".format(self.x, self.y)

    def to_dict(self) -> dict:
        return {
            "x": self.x.id,
            "y": self.y.id
        }
