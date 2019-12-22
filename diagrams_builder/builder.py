from typing import List, Any, Callable

from diagrams_builder.diagram_data import DiagramData
from diagrams_builder.point import Point
from diagrams_builder.link import Link
import equation_parser as ep
import itertools


def build_diagram(equation: str, dataset: list) -> DiagramData:
    parsed_equation = ep.process_str(equation)
    points = parse_dataset(dataset)

    links = calculate_all_links(points, parsed_equation)
    remove_transitive_links(links)

    calculate_ranks(points, links)

    return DiagramData(points, links)


def parse_dataset(dataset: list) -> list:
    return [Point(index, elem) for index, elem in enumerate(dataset)]


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
    find_links_witch_begins_with: Callable[[Any], List[Any]] = lambda p: list(filter(lambda l: l.x == p, links))
    find_links_witch_end_with: Callable[[Any], List[Any]] = lambda p: list(filter(lambda l: l.y == p, links))

    def calculate_child_nodes_ranks(p: Point):
        begin_with = find_links_witch_begins_with(p)
        for link in begin_with:
            child_point: Point = link.y
            child_point.rank = p.rank + 1
            calculate_child_nodes_ranks(child_point)

    bottom_points = list(filter(lambda p: len(find_links_witch_end_with(p)) == 0, points))
    for point in bottom_points:
        point.rank = 0
        calculate_child_nodes_ranks(point)
