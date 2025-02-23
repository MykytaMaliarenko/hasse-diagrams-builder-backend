from math import sin, cos
from typing import List, Any, Callable

from diagrams_builder.diagram_data import DiagramData
from diagrams_builder.points import Point, QuasiPoint, BasicPoint
from diagrams_builder.link import Link
import equation_parser as ep
import itertools

find_links_witch_begins_with: Callable[[Any], List[Any]] = lambda p, links: list(filter(lambda l: l.x == p, links))
find_links_witch_end_with: Callable[[Any], List[Any]] = lambda p, links: list(filter(lambda l: l.y == p, links))

find_links_witch_are_quasi: Callable = lambda l, links: \
    list(filter(lambda inner_l: inner_l.y == l.x, find_links_witch_begins_with(l.y, links)))


def build_diagram(equation: str, dataset: list) -> DiagramData:
    parsed_equation = ep.process_str(equation)
    points = parse_dataset(dataset)

    links = calculate_all_links(points, parsed_equation)

    if is_quasi_order(links):
        print("quasi")
        while is_quasi_order(links):
            points = combine_quasi_points(points, links)
            links = calculate_all_links(points, parsed_equation)

    remove_transitive_links(links)
    calculate_ranks(points, links)
    return DiagramData(points, links)


def parse_dataset(dataset: list) -> list:
    return [BasicPoint(index, elem) for index, elem in enumerate(dataset)]


def calculate_all_links(points: list, equation: str) -> list:
    links = list()

    for combination in list(itertools.permutations(points, 2)):
        a: Point = combination[0]
        b: Point = combination[1]

        x = a.value
        y = b.value
        if eval(equation):
            links.append(Link(a, b))

    return links


def is_quasi_order(links: list) -> bool:
    return not len(list(
            filter(lambda l: len(find_links_witch_are_quasi(l, links)) != 0, links)
    )) == 0


def combine_quasi_points(points: list, links: list) -> list:
    res = []

    quasi_links = list(filter(lambda l: find_links_witch_are_quasi(l, links), links))
    for i, link in enumerate(quasi_links):
        has_x_in_other_quasi = len(list(filter(lambda qp: link.x in qp, res))) != 0
        has_y_in_other_quasi = len(list(filter(lambda qp: link.y in qp, res))) != 0

        if has_x_in_other_quasi and not has_y_in_other_quasi:
            list(filter(lambda qp: link.x in qp, res))[0] += link.y
        elif has_y_in_other_quasi and not has_x_in_other_quasi:
            list(filter(lambda qp: link.y in qp, res))[0] += link.x
        elif not has_x_in_other_quasi and not has_y_in_other_quasi:
            res.append(QuasiPoint(id=i, points=[link.x, link.y]))

    free_points = list(filter(lambda p: len(list(filter(lambda qp: p in qp, res))) == 0, points))
    for i, point in enumerate(free_points):
        point.id = len(quasi_links) + i
        res.append(point)

    return res


def remove_transitive_links(links: list):
    index = 0
    while index < len(links):
        link = links[index]
        if path_exists(links[:index] + links[index + 1:], link.x, link.y):
            links.pop(index)
        else:
            index += 1


def path_exists(links: list, x: Point, y: Point) -> bool:
    res_links = list(filter(lambda l: l.x == x, links))
    if len(res_links) == 0:
        return False
    else:
        for index, link in enumerate(res_links):
            if link.y == y:
                return True

            if path_exists(links, link.y, y):
                return True

        return False


def calculate_ranks(points: List[Point], links: List[Link]):
    def calculate_child_nodes_ranks(p: Point):
        begin_with = find_links_witch_begins_with(p, links)
        for link in begin_with:
            child_point: Point = link.y
            child_point.rank = p.rank + 1
            calculate_child_nodes_ranks(child_point)

    bottom_points = list(filter(lambda p: len(find_links_witch_end_with(p, links)) == 0, points))
    for point in bottom_points:
        point.rank = 0
        calculate_child_nodes_ranks(point)
