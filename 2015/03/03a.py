from helpers import get_input as gi
import copy

inputArr = [*gi.get_input()]

moves_mapping = {'^': {'x': 0, 'y': -1}, '>': {'x': 1, 'y': 0},
                 'v': {'x': 0, 'y': 1}, '<': {'x': -1, 'y': 0}}

santa_position = {'x': 0, 'y': 0}

visited_houses = set()


def move_santa(position, move):
    position_change = moves_mapping[move]
    moved = copy.deepcopy(position)
    moved['x'] += position_change['x']
    moved['y'] += position_change['y']

    house = f"{moved['x']},{moved['y']}"
    visited_houses.add(house)

    return moved


for move in inputArr:
    santa_position = move_santa(santa_position, move)

print(f"the answer is {len(visited_houses)}")
