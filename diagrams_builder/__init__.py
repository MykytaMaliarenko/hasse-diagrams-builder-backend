from diagrams_builder.diagram_data import DiagramData
import equation_parser as ep
import diagrams_builder.builder as builder


def build_diagram(equation: str, dataset: list) -> DiagramData:
    parsed_equation = ep.process_str(equation)
    points = builder.parse_dataset(dataset)

    links = builder.calculate_all_links(points, parsed_equation)
    builder.remove_transitive_links(links)

    return DiagramData(points, links)
