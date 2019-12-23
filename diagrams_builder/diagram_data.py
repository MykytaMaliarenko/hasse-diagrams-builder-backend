class DiagramData:
    points: list
    links: list

    def __init__(self, points: list, links: list):
        self.points = points
        self.links = links

    def to_dict(self) -> dict:
        points_sorted_by_rank = list()

        i = 0
        temp = list(filter(lambda p: p.rank == i, self.points))
        while len(temp) > 0:
            points_sorted_by_rank.append(temp)
            i += 1
            temp = list(filter(lambda p: p.rank == i, self.points))

        points_json = list(map(lambda line: list(map(lambda p: p.dict, line)), points_sorted_by_rank))

        links_json = list()
        [links_json.append(el.to_dict()) for el in self.links]

        return {
            "points": points_json,
            "links": links_json
        }
