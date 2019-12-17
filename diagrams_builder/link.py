import diagrams_builder.point as p


class Link:
    x: p.Point
    y: p.Point

    def __init__(self, x: p.Point, y: p.Point):
        self.x = x
        self.y = y

    def __repr__(self):
        return "{} -> {}".format(self.x, self.y)

    def to_dict(self) -> dict:
        return {
            "x": self.x.id,
            "y": self.y.id
        }
