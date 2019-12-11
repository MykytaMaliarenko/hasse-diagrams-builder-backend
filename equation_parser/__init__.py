import math
from equation_parser.power import parse_power
from equation_parser.trigonometry import parse_trigonometry
from equation_parser.abs import parse_abs

parsers = [
    parse_power,
    parse_trigonometry,
    parse_abs
]


def process_str(inp: str) -> str:
    for parser in parsers:
        inp = parser(inp)

    return inp


if __name__ == "__main__":
    print(process_str("arcsin(x^2)^2 + |y^5|"))


