from helpers import get_input as gi

input = gi.get_input().splitlines()


def calculate_paper(l: int, w: int, h: int):
    side1 = 2 * l * w
    side2 = 2 * w * h
    side3 = 2 * h * l

    smallest_side = min([side1, side2, side3]) // 2

    return side1 + side2 + side3 + smallest_side


total_feet = 0

for present in input:
    [l, w, h] = map(int, present.split('x'))

    total_feet += calculate_paper(l, w, h)


print('solution is:', total_feet)
