from .exceptions import ParsingException


def parse_binary_operation(expression):
    expression = expression.strip()
    try:
        first, operator, second = expression.split()
    except ValueError:
        raise ParsingException(
            'Could not parse expression "{}"'.format(expression))
    return [operator, first, second]


def parse_unary_operation(expression):
    expression = expression.strip()
    try:
        operator, second = expression.split()
    except ValueError:
        raise ParsingException(
            'Could not parse expression "{}"'.format(expression))
    return [operator, second]
