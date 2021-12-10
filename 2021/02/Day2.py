import os

# Author: Cole Polyak
# 2 December 2021
# Advent of Code: Day 2
#
# There are definitely lurking improvements that can be made here, and we could
# probably combine part1 & part2 and calculate both at the same time to only loop
# once but ¯\_(ツ)_/¯

def main():
    arr = parse_input("day2.txt")
    part1(arr)
    part2(arr)

def part1(arr):
    depth = 0
    forward = 0

    # O(n)
    for direction, count in arr:
        if direction == "forward":
            forward += count

        if direction == "down":
            depth += count

        if direction == "up":
            depth -= count

    print(f"Part 1: Depth {depth}, Forward {forward}, Final {depth * forward}")


def part2(arr):
    aim = 0
    depth = 0
    forward = 0

    # O(n)
    for direction, count in arr:
        if direction == "forward":
            forward += count
            depth += (aim * count)

        if direction == "down":
            aim += count

        if direction == "up":
            aim -= count
    print(f"Part 2: Depth {depth}, Forward {forward}, Final {depth * forward}")


def parse_input(filename):
    file = open(f"{os.getcwd()}/{filename}", "r")
    arr = []

    for line in file:
        line = line.split(" ")
        item = (line[0].strip(), int(line[1].strip()))
        arr.append(item)
    file.close()
    return arr

if __name__ == '__main__':
    main()
