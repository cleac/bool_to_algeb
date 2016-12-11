from .parser import parse
from .convert import convert
from .to_str import to_str


def process_expression(expression):
    parsed = parse(expression)
    converted = convert(parsed)
    return to_str(converted)
