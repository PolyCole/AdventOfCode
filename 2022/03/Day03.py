import os

# Author: Cole Polyak
# 03 December 2022
# Advent of Code: Day 03

def main():
    arr = parse_input("day03.txt")

    part1(arr)
    part2(arr)

def get_char_set(str):
    chars = set()

    for char in str:
        chars.add(char)
    
    return chars

def get_char_score(char):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96

def part1(arr):
    score = 0

    for rucksack in arr:
        first, second = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        
        compartment_one = get_char_set(first)
        compartment_two = get_char_set(second)

        overlap = compartment_one.intersection(compartment_two)
        
        for item in overlap:
            score += get_char_score(item)
    
    print(f"Score Part 1:: {score}")

def part2(arr):
    score = 0

    while len(arr) != 0:
        # We'll just approach this backwards. Output is divisible by 3
        # so we're good here.
        one = get_char_set(arr.pop())
        two = get_char_set(arr.pop())
        three = get_char_set(arr.pop())

        aggregate = (one.intersection(two)).intersection(three)

        for char in aggregate:
            score += get_char_score(char)
    
    print(f"Score Part 2:: {score}")


def parse_input(filename):
    file = open(f"{os.getcwd()}/03/{filename}", "r")
    arr = []

    for line in file:
        arr.append(line.strip())

    file.close()
    return arr

if __name__ == '__main__':
    main()
