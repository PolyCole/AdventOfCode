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
    print("Start")
    args = get_args()

    today = datetime.date.today()
    year = today.year

    with console.status(f':christmas_tree: Building day {args.day} of Advent Of Code {year}') as status:
        cur_dir = os.getcwd()

        sleep(2)
        part_one = f'{cur_dir}/{year}'
        if not os.path.exists(part_one):
            os.mkdir(part_one)

        desired_dir = f'{cur_dir}/{year}/{args.day}'
        if not os.path.exists(desired_dir):
            os.mkdir(desired_dir)
        console.log(f':file_folder: Created new working directory...')

        sleep(2)
        new_file_path = f'{desired_dir}/Day{args.day}.py'
        with open(f'{cur_dir}/template.py', "rt") as fin:
            with open(new_file_path, "wt") as fout:
                for line in fin:
                    fout.write(line.replace('XX', args.day))

        console.log(":page_facing_up: Created new working file...")

        sleep(2)
        input_file = open(f'{desired_dir}/day{args.day}.txt', "w")
        console.log(":memo: Created new input file...")

        sleep(2)
        console.log(console.log(":christmas_tree: Day creation complete! Happy coding :slightly_smiling_face:"))
        subprocess.run(["code", part_one])
        return

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