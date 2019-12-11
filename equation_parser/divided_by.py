import re


def replace_func(match):
    match_str: str = match[0]
    return "({})%({}) == 0".format(match_str[:match_str.index("::")], match_str[match_str.index("::") + 3:])


def parse_divided_by(inp: str) -> str:
    return re.sub(r"^.+::.+$", replace_func, inp)