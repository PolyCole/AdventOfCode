import os

# Author: Cole Polyak
# 10 December 2021
# Advent of Code: Day 10

def main():
    arr = parse_input("day10.txt")
    part1(arr)
    print(f"-------------")
    part2(arr)



def part2(arr):
    openers = "([{<"
    closers = ")]}>"
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }
    lookups = [(')', 1), (']', 2), ('}', 3), ('>', 4)]

    sums = []

    for line in arr:
        stack = []
        sum = 0
        try:
            for char in line:
                if char in openers:
                    stack.append(char)
                else:
                    popped = stack.pop()
                    if popped != pairs[char]:
                        raise StopIteration

            while(len(stack) != 0):
                item = stack.pop()
                character, value = lookups[openers.find(item)]
                sum *= 5
                sum += value

            sums.append(sum)
        except StopIteration:
            # corrupted string, let's ignore it.
            1 == 1

    sums = sorted(sums)
    print(f"{sums[int((len(sums) / 2) - 0.5)]}")

def part1(arr):
    openers = "([{<"
    closers = ")]}>"
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }
    lookups = {')': 3, ']': 57, '}': 1197, '>': 25137}
    stack = []

    sum = 0

    for line in arr:
        for char in line:
            if char in openers:
                stack.append(char)
            elif char in closers:
                popped = stack.pop()
                if popped != pairs[char]:
                    sum += lookups[char]
            else:
                print(f"UNSURE HOW YOU GOT HERE")

    print(f"{sum}")


def parse_input(filename):
    file = open(f"{os.getcwd()}/{filename}", "r")
    arr = []

    for line in file:
        arr.append(line.strip())

    return arr

if __name__ == '__main__':
    main()
