#!/usr/bin/env python3
import sys

from collections import OrderedDict

from lab import process_expression


CALL_VARIANTS = (
    lambda x, y: '{} and {}'.format(x, y),
    lambda x, y: '{} or {}'.format(x, y),
)
FUNCTIONS_BANK = OrderedDict()


def systolic_processor(
        target_depth,
        current_depth=1,
        current_level=1,
        current_str='x0'):
    cur_variable = 'x{}'.format(current_depth)
    if current_str != 'x0':
        current_str = '({})'.format(current_str)
    strs = (
        CALL_VARIANTS[0](current_str, cur_variable),
        CALL_VARIANTS[1](current_str, cur_variable)
    )
    if current_depth < target_depth - 1:
        strs = [
            systolic_processor(
                target_depth,
                current_depth + 1,
                current_level + (1 - num),
                str_)
            for num, str_ in enumerate(strs)
        ]
    else:
        strs = list(strs)
        upper_level_repr = 'y{}'.format(current_level + 1)
        cur_level_repr = 'y{}'.format(current_level)
        if upper_level_repr not in FUNCTIONS_BANK:
            FUNCTIONS_BANK[upper_level_repr] = []
        if cur_level_repr not in FUNCTIONS_BANK:
            FUNCTIONS_BANK[cur_level_repr] = []
        FUNCTIONS_BANK[upper_level_repr].append(strs[0])
        FUNCTIONS_BANK[cur_level_repr].append(strs[1])
    return FUNCTIONS_BANK


def process_processor_logic():
    for key, lst in FUNCTIONS_BANK.items():
        print('\n{}\n============================'.format(key))
        for item in lst:
            print(item)
            processed = process_expression(item)
            print(processed)
            print('-' * 20)


if __name__ == '__main__':
    try:
        item = int(sys.argv[1])
    except IndexError:
        item = 5
    proc_logic = systolic_processor(item)
    process_processor_logic()
