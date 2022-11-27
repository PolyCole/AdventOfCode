# Here's what we want to do.


# 7. Output to terminal and open file and input file in atom (maybe using a)
from argparse import ArgumentParser
from time import sleep
from rich.console import Console
from rich.markdown import Markdown
import datetime
import shutil
import os
import subprocess

console = Console()

def main():
    args = get_args()

    year = datetime.date.today().year
    day = args.day

    with console.status(f':christmas_tree: Building day {day} of Advent Of Code {year}') as status:
        cur_dir = os.getcwd()
        year_dir = f'{cur_dir}/{year}'
        day_dir = f'/{year_dir}/{day}'

        # Creating directories
        sleep(2)
        create_dir(year_dir)
        create_dir(day_dir)
        console.log(f':file_folder: Created new working directory...')

        # Creating working file
        sleep(2)
        create_working_file(cur_dir, day_dir, day)
        console.log(":page_facing_up: Created new working file...")

        # Creating input file
        sleep(2)
        input_file = open(f'{day_dir}/day{day}.txt', "w")
        console.log(":memo: Created new input file...")

        # Opening in VSCode and exiting.
        sleep(2)
        console.log(console.log(":christmas_tree: Day creation complete! Happy coding :slightly_smiling_face:"))
        subprocess.run(["code", year_dir])
        return

def create_dir(new_dir):
    if not os.path.exists(new_dir):
            os.mkdir(new_dir)


def create_working_file(cur_dir, day_dir, day):
        with open(f'{cur_dir}/template.py', "rt") as fin:
            with open(f'{day_dir}/Day{day}.py', "wt") as fout:
                for line in fin:
                    fout.write(line.replace('XX', day))


def get_args():
    parser = ArgumentParser(prog='aoc_template', description="A script to create a new template for AdventOfCode")
    parser.add_argument('-d', '--day', help="Which day we're creating", required=True)
    args = parser.parse_args()

    validate_arg(args)
    return args


def validate_arg(args):
    try:
        if int(args.day) > 25 or int(args.day) <= 0:
            raise TypeError("Valid day range is between 1-25. Please make sure you're between then.")
    except TypeError as e:
        console.log(f":x: {e}")
        exit(1)



if __name__ == '__main__':
    main()