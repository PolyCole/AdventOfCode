import os

# Author: Cole Polyak
# 01 December 2024
# Advent of Code: Day 01

def main():
    arr = parse_input("day01.txt")
    arr_formatted = format_input(arr)

    part1(arr_formatted)
    part2(arr_formatted)

def part1(arr):
    left = []
    right = []

    for pair in arr:
        left.append(pair[0])
        right.append(pair[1])

    left.sort()
    right.sort()

    diff = 0

    for i in range(len(left)):
        diff += abs(right[i] - left[i])

    print(f'PART 1 ANSWER: {diff}')

def part2(arr):    
    left = []
    rightFreqMap = {}

    for line in arr:
        left.append(line[0])

        if line[1] in rightFreqMap:
            rightFreqMap[line[1]] += 1
        else:
            rightFreqMap[line[1]] = 1

    total = 0
    
    for i in range(len(left)):
        total += left[i] * rightFreqMap.get(left[i], 0)

    print(f'PART 2 ANSWER: {total}')

def format_input(arr):
    formatted = []
    for line in arr:
        split = line.split("   ")
        formatted.append(list(map(int, split)))
    
    return formatted

def parse_input(filename):
    file = open(f"{os.getcwd()}/01/{filename}", "r")
    arr = []

    for line in file:
        arr.append(line.strip())

    file.close()
    return arr

if __name__ == '__main__':
    main()
