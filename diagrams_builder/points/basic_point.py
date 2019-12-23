from .point import Point


class BasicPoint(Point):
    id: int
    v: float
    rank: int

    def __init__(self, id: int, value: float):
        self.id = id
        self.v = value
        self.rank = -1

    def __eq__(self, other):
        if isinstance(other, BasicPoint):
            return other.id == self.id and other.value == self.value
        else:
            return False

    def __repr__(self):
        if self.rank != -1:
            return "(id: {} value: {} rank: {})".format(self.id, self.value, self.rank)
        else:
            return "(id: {} value: {})".format(self.id, self.value)

    @property
    def value(self) -> float:
        return self.v

    @property
    def dict(self) -> dict:
        return {
            "id": self.id,
            "value": self.value,
            "rank": self.rank
        }
