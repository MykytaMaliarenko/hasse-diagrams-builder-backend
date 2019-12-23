from .point import Point
from .basic_point import BasicPoint


class QuasiPoint(Point):
    id: int
    points: list
    rank: int

    def __init__(self, id: int, points: list):
        self.id = id
        self.points = points
        self.rank = -1

    def __eq__(self, other):
        if isinstance(other, QuasiPoint):
            return len(list(filter(lambda p: p not in self.points, other.points))) == 0
        else:
            return False

    def __contains__(self, item):
        if isinstance(item, BasicPoint):
            return item in self.points
        else:
            return False

    def __repr__(self):
        return "(id: {} rank: {} points: {})".format(self.id, self.rank, self.pretty_value)

    def __add__(self, other):
        if isinstance(other, BasicPoint):
            self.points.append(other)

    @property
    def value(self) -> float:
        return self.points[0].value if len(self.points) > 0 else 0

    @property
    def pretty_value(self) -> str:
        return "{" + ",".join([str(p.value) for p in self.points]) + "}"

    @property
    def dict(self) -> dict:
        return {
            "id": self.id,
            "value": self.pretty_value,
            "rank": self.rank
        }
