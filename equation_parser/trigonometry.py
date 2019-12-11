import re

patterns_to_replace = {
    "arcsin": "asin",
    "asrccos": "acos",
    "arctg": "atan",
    "tg": "tan",
}


def parse_trigonometry(inp: str) -> str:
    for pattern, replace_to in patterns_to_replace.items():
        inp = re.sub(pattern, replace_to, inp)
    return inp
