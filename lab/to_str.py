from .const import ITERABLE_TYPES
from .exceptions import OperatorNotFoundError

TRANSLATIONS = {
    'and': lambda x, y: '{} and {}'.format(x, y),
    'or': lambda x, y: '{} or {}'.format(x, y),
    'not': lambda x: 'not {}'.format(x),
    '*': lambda x, y: '{} * {}'.format(x, y),
    '/': lambda x, y: '{} / {}'.format(x, y),
    '+': lambda x, y: '{} + {}'.format(x, y),
    '-': lambda x, y: '{} - {}'.format(x, y),
}


def to_str(argument):
    operator, *args = argument
    if operator not in TRANSLATIONS:
        raise OperatorNotFoundError(operator)
    for pos, arg in enumerate(args):
        arg_type = type(arg)
        if arg_type in ITERABLE_TYPES:
            args[pos] = '({})'.format(to_str(arg))
    return TRANSLATIONS[operator](*args)
