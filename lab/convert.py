from .const import ITERABLE_TYPES
from .exceptions import OperatorNotFoundError

TRANSLATIONS = {
    'and': lambda x, y: ['*', x, y],
    'or': lambda x, y: ['-', ['+', x, y], ['*', x, y]],
    'not': lambda x: ['-', '1', x],
}


def convert(argument):
    operator, *args = argument
    if operator not in TRANSLATIONS:
        raise OperatorNotFoundError(operator)
    for pos, arg in enumerate(args):
        arg_type = type(arg)
        if arg_type in ITERABLE_TYPES:
            args[pos] = convert(arg)
    return TRANSLATIONS[operator](*args)
