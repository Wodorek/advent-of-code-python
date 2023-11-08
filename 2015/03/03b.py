from helpers import get_input as gi

input = gi.get_input()

split = list(input)

houses_dict = {

}

curr_x = 0
curr_y = 0


def move_santa(direction):

    global curr_x
    global curr_y

    if direction == '^':
        curr_x += 1

    if direction == "v":
        curr_x -= 1

    if direction == '>':
        curr_y += 1

    if direction == "<":
        curr_y -= 1

    houses_key = f'{curr_x},{curr_y}'

    if houses_key in houses_dict:
        houses_dict[houses_key] += 1

    else:

        houses_dict[houses_key] = 1


santa_moves = []
robo_santa_moves = []


for index, dir in enumerate(split):
    if index % 2 == 0:
        santa_moves.append(dir)
    else:
        robo_santa_moves.append(dir)


for move in santa_moves:
    move_santa(move)

curr_x = 0
curr_y = 0

for move in robo_santa_moves:
    move_santa(move)


print(len(houses_dict.keys()))
