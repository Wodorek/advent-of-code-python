from helpers import get_input as gi

input = gi.get_input().splitlines()


def calculate_paper(l: int, w: int, h: int):
    bow = l*w*h

    sorted_vals = sorted([l, w, h])

    return bow + (sorted_vals[0] * 2) + (sorted_vals[1] * 2)


total_feet = 0

for present in input:
    [l, w, h] = map(int, present.split('x'))

    total_feet += calculate_paper(l, w, h)


print('solution is:', total_feet)
