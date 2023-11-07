from helpers import get_input as gi
from pathlib import Path

path = Path.cwd()

input = gi.get_input()

split = list(input)

curr_floor = 0
char_position = 1

for el in split:

    if el == '(':
        curr_floor += 1
    else:
        curr_floor -= 1

    if curr_floor == -1:
        break

    char_position += 1

print('solution:', char_position)
