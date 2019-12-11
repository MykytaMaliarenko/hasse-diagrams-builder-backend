import re


def parse_power(inp: str) -> str:
    return re.sub("\\^", "**", inp)
