import json


class DiagramData:
    points: list
    links: list

    def __init__(self, points: list, links: list):
        self.points = points
        self.links = links

    def to_dict(self) -> dict:
        points_json = list()
        [points_json.append(el.to_dict()) for el in self.points]

        links_json = list()
        [links_json.append(el.to_dict()) for el in self.links]

        return {
            "points": points_json,
            "links": links_json
        }
