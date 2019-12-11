class DiagramData:
    points: list
    links: list

    def __init__(self, points: list, links: list):
        self.points = points
        self.links = links

    def to_json(self) -> str:
        pass
