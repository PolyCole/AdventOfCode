import os

# Author: Cole Polyak
# 10 December 2022
# Advent of Code: Day 10

def main():
    arr = parse_input("day10.txt")
    
    sprite = 1
    clock = 0
    line = []

    for instruction in arr:
        if len(instruction) == 1:
            line.append(add_char(sprite, clock))
            clock += 1
        else:
            line.append(add_char(sprite, clock))
            clock += 1

            if clock % 40 == 0:
                print(f"{''.join(line)}")
                line = []
                clock = 0

            line.append(add_char(sprite, clock))
            sprite += int(instruction[1])
            clock += 1

        if clock % 40 == 0:
            print(f"{''.join(line)}")
            line = []
            clock = 0

def add_char(sprite, clock):
    if clock in range(sprite - 1, sprite + 2):
        return "#"
    else:
        return "."


def part1(arr):
    x = 1
    clock = 1
    sums = []

    for instruction in arr:
        if len(instruction) == 1:
            clock += 1
        else:
            clock += 1
            is_target_cycle(clock, sums, x)
            x += int(instruction[1])
            clock += 1
        
        is_target_cycle(clock, sums, x)
    
    print(f"SUMS: {sums}")
    print(f"SUM SUM SUM:::: {sum(sums)}")

def is_target_cycle(clock, sums, x):
    if clock in [20, 60, 100, 140, 180, 220]:
        sums.append(x * clock)


def parse_input(filename):
    file = open(f"{os.getcwd()}/2022/10/{filename}", "r")
    arr = []

    for line in file:
        arr.append(line.strip().split(" "))

    file.close()
    return arr

if __name__ == '__main__':
    main()
