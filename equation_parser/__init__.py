import math
from equation_parser.power import parse_power
from equation_parser.trigonometry import parse_trigonometry
from equation_parser.abs import parse_abs
from equation_parser.divided_by import parse_divided_by
from equation_parser.mod import parse_mod

parsers = [
    parse_power,
    parse_trigonometry,
    parse_abs,
    parse_mod,
    parse_divided_by
]


def process_str(inp: str) -> str:
    for parser in parsers:
        inp = parser(inp)

    return inp


if __name__ == "__main__":
    print(process_str("4mod(x)::4mod(y)"))


