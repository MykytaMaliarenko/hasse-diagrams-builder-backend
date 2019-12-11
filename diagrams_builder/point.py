class Point:
    id: int
    value: float

    def __init__(self, id: int, value: float):
        self.id = id
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Point):
            return other.id == self.id
        else:
            return False

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "value": self.value
        }
