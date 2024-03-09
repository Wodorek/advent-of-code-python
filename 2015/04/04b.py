from helpers import get_input as gi
import hashlib

input_str = gi.get_input().strip()

tested_num = 0


while True:
    test_string = f'{input_str}{tested_num}'
    hashed = hashlib.md5(f'{test_string}'.encode()).hexdigest()
    if hashed[:5:] == '000000':
        break

    tested_num += 1

print(f'answer is {tested_num}')
