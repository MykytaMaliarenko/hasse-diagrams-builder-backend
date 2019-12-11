import re

regex_pattern = r"\|\w+\|"


def replace_func(match):
    return "abs(" + match[0][1:-1] + ")"


def parse_abs(inp: str) -> str:
    return re.sub(r"\|[\w*\s]+\|", replace_func, inp)
