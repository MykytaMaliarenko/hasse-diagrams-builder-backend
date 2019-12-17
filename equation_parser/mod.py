import re


def replace_mod(match) -> str:
    match_str: str = match[0]
    match_str = match_str.replace("mod(", "%")
    return match_str[:-1]


def parse_mod(text: str) -> str:
    return re.sub(r"[\d\w]+mod\([\d\s\w]+\)", replace_mod, text)
