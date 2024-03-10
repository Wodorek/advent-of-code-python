from helpers import get_input as gi

strings_list = gi.get_input().splitlines()

vowels = ["a", "e", "i", "o", "u"]
disallowed = ['ab', 'cd', 'pq', 'xy']


def is_string_nice(str):
    vowels_count = 0
    has_double = False

    for idx, letter in enumerate([*str]):
        if letter in vowels:
            vowels_count += 1
        if idx + 1 < len(str):
            if letter == str[idx + 1]:
                has_double = True

    for substr in disallowed:
        if substr in str:
            return False

    return vowels_count >= 3 and has_double


nice_strings_count = 0

for str in strings_list:
    if is_string_nice(str):
        nice_strings_count += 1


print(f'the answer is {nice_strings_count}')
