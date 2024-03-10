from helpers import get_input as gi

strings_list = gi.get_input().splitlines()


def is_string_nice(str):
    pairs = []
    has_repeat = False

    for idx, char in enumerate(str):
        if idx+1 < len(str) and len(set(str[idx:idx+2:])) > 1:
            pairs.append(f'{char}{str[idx+1]}')
        if idx + 2 < len(str):
            if char == str[idx+2]:
                has_repeat = True

    pairs_set = set(pairs)

    has_pair = len(pairs) > len(pairs_set)

    return has_repeat and has_pair


nice_strings_count = 0

for str in strings_list:
    if is_string_nice(str):
        nice_strings_count += 1


print(f'the answer is {nice_strings_count}')
