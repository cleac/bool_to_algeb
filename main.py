#!/usr/bin/env python3
import sys

from lab import process_expression
from lab.exceptions import ParsingException

if __name__ == '__main__':
    items = []
    try:
        for arg in sys.argv[1:]:
            items.append(process_expression(arg))
    except ParsingException as e:
        print(e)
        sys.exit(-1)
    for i in items:
        print(i)
