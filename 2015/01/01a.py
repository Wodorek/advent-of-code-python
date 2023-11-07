from helpers import get_input as gi

input = gi.get_input()

split = list(input)

curr_floor = 0

for el in split:
    if el == '(':
        curr_floor += 1
    else:
        curr_floor -= 1

print('solution:', curr_floor)
