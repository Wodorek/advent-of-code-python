from helpers import get_input as gi

direction_strings = gi.get_input().splitlines()


def parse_data(str: str):
    split_str = str.split()

    if split_str[0] == 'toggle':
        return [list(map(int, split_str[1].split(','))),
                list(map(int, split_str[3].split(',')))]

    return [list(map(int, split_str[2].split(','))), list(map(int, split_str[4].split(','))), split_str[1]]


lights = []

for i in range(0, 999):
    lights.append([0]*1000)

parsed_inst = list(map(parse_data, direction_strings))


def change_lights(lights, start, end, mode=None):
    startX, startY = start
    endX, endY = end

    for i in range(startX, endX + 1):
        for j in range(startY, endY + 1):
            if mode == None:
                if lights[j][i] == 0:
                    lights[j][i] = 1
                else:
                    lights[j][i] = 0
            elif mode == 'on':
                lights[j][i] = 1
            else:
                lights[j][i] = 0


for command in parsed_inst:

    change_lights(lights, *command)

on_count = 0

for row in lights:
    for cell in row:
        if cell == 1:
            on_count += 1

print(on_count)
