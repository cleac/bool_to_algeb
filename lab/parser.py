import re

from .exceptions import ParsingException
from .operations import parse_unary_operation
from .operations import parse_binary_operation
from .const import ITERABLE_TYPES

PARSING_FUNCTIONS = (
    parse_unary_operation,
    parse_binary_operation,
)

OPEN_BRACKET = '('
CLOSE_BRACKET = ')'
CURRENT_INDEX = 0

ALIAS_POOL = {
}


def find_and_process_brackets(expression, start_from=0):
    global CURRENT_INDEX
    br_open_pos = expression.find(OPEN_BRACKET, start_from)
    if br_open_pos < 0:
        return expression
    current_level = 1
    br_close_pos = 0
    for i in range(br_open_pos + 1, len(expression)):
        if expression[i] == OPEN_BRACKET:
            current_level += 1
        elif expression[i] == CLOSE_BRACKET:
            current_level -= 1
            if current_level == 0:
                br_close_pos = i
                break
    else:
        raise ParsingException(
            'Invalid parenthis in expression "{}"'.format(expression))
    extracted = expression[br_open_pos:br_close_pos+1]
    replace_id = '$<{}>'.format(CURRENT_INDEX)
    CURRENT_INDEX += 1
    expr_new = expression.replace(extracted, replace_id)
    ALIAS_POOL[replace_id] = parse(extracted[1:-1])
    return find_and_process_brackets(expr_new, br_open_pos + len(replace_id))


ALIAS_RE = re.compile('\$\<\d+\>')


def replace_alias(expressions):
    for pos, expr in enumerate(expressions):
        expr_type = type(expr)
        if expr_type in ITERABLE_TYPES:
            expressions[pos] = replace_alias(expr)
        elif ALIAS_RE.match(expr):
            expressions[pos] = ALIAS_POOL[expr]
    return expressions


def parse(expression):
    expression = find_and_process_brackets(expression)
    for func in PARSING_FUNCTIONS:
        try:
            result = func(expression)
        except ParsingException:
            continue
        else:
            break
    else:
        raise ParsingException(
            'Could not parse expression "{}"'.format(expression))
    operator, *args = result
    args = replace_alias(args)
    return [operator] + args
