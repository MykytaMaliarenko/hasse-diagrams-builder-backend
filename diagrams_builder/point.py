class Point:
    id: int
    value: float
    rank: int

    def __init__(self, id: int, value: float):
        self.id = id
        self.value = value
        self.rank = -1

    def __eq__(self, other):
        if isinstance(other, Point):
            return other.id == self.id
        else:
            return False

    def __repr__(self):
        return "(id: {} value: {} rank: {})".format(self.id, self.value, self.rank)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "value": self.value,
            "rank": self.rank
        }
