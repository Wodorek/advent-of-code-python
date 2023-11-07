from helpers import get_input as gi
from pathlib import Path

path = Path.cwd()

input = gi.get_input(2015, 1, path)

split = list(input)

curr_floor = 0

for el in split:
    if el == '(':
        curr_floor += 1
    else:
        curr_floor -= 1

print('solution:', curr_floor)
