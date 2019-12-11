from diagrams_builder.diagram_data import DiagramData
from diagrams_builder.point import Point
from diagrams_builder.link import Link
import equation_parser as ep
import itertools

X_VARIABLE_NAME = "x"
Y_VARIABLE_NAME = "y"


def build_diagram(equation: str, dataset: list) -> DiagramData:
    parsed_equation = ep.process_str(equation)
    points = parse_dataset(dataset)

    links = calculate_all_links(points, parsed_equation)
    remove_transitive_links(links)

    return DiagramData(points, links)


def parse_dataset(dataset: list) -> list:
    return [Point(index, elem) for index, elem in enumerate(dataset)]


def calculate_all_links(points: list, equation: str) -> list:
    links = list()

    for combination in list(itertools.combinations(points, 2)):
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
    res_links = list(filter(lambda link: link.x == x, links))
    if len(res_links) == 0:
        return False
    else:
        for index, link in enumerate(res_links):
            if link.y == y:
                return True

            if path_exists(res_links[:index] + res_links[index + 1:], link.x, y):
                return True

        return False
