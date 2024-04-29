from helpers import get_input as gi

input = gi.get_input().splitlines()


alphabet = list('abcdefghijklmnopqrstuvwxyz')


forbidden = []


for idx, letter in enumerate(alphabet):
    if idx + 1 >= len(alphabet):
        break

    forbidden.append(f'{letter}{alphabet[idx+1]}')


print(forbidden)


def is_nice(str):

    letters_list = list(str)
    print(letters_list)
    vowels_list = ['a', 'e', 'i', 'o', 'u']

    vowels = 0
    has_double = False
    has_forbidden = False

    for idx, letter in enumerate(letters_list):

        if letter in vowels_list:
            vowels += 1

        if idx + 1 >= len(letters_list):
            break

        if f'{letter}{letters_list[idx + 1]}' in forbidden:
            has_forbidden = True

        if letter == letters_list[idx + 1]:
            has_double = True

    return {'forbid': has_forbidden, 'double': has_double, 'vowels': vowels}


print(is_nice(input[1]))
