

class ParsingException(Exception):
    def __init__(self, message, *args, **kargs):
        super().__init__(message, *args, **kargs)


class OperatorNotFoundError(Exception):
    def __init__(self, operator, *args, **kargs):
        super().__init__(
            'Operator "{}" not found'.format(operator),
            *args,
            **kargs
        )
