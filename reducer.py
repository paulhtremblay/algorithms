#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

def _print_line(current_word, current_count):
    print('{current_word}\t{current_count}'.format(current_word = current_word, current_count = current_count))

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    word, count = line.strip().split('\t', 1)
    count = int(count)

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_count:
            # write result to STDOUT
            _print_line(current_word, current_count)
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    _print_line(current_word, current_count)

