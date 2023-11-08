from helpers import get_input as gi
import hashlib

input = gi.get_input().strip()


def find_hash(num):

    hash_str = f'{input}{num}'
    hashed = hashlib.md5(hash_str.encode('utf-8'))

    return hashed.hexdigest()


found_hash = ''
curr_idx = 0

while True:
    if found_hash[0:5] == '00000':
        break
    else:
        curr_idx += 1
        found_hash = find_hash(curr_idx)


print(curr_idx)
