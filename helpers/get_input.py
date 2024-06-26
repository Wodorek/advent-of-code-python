import os
import requests
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()


def get_input():

    path = Path.cwd()

    path_string = path.as_posix().split('/')

    file_path = f'{path}\\input.txt'
    input_txt = open(file_path, "a+")

    if os.stat(input_txt.name).st_size == 0:
        print('downloading input')
        url = f'https://adventofcode.com/{path_string[-2]}/day/{path_string[-1].lstrip("0")}/input'

        print(url)
        session_id = os.getenv('SESSION_ID')
        resp = requests.get(
            url, cookies={"session": session_id})  # type: ignore
        input_txt.write(resp.text)

    input_txt.seek(0)
    return input_txt.read()
