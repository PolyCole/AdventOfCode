import os

# Author: Cole Polyak
# 13 December 2022
# Advent of Code: Day 13

def main():
    arr = parse_input("day13-test.txt")
    print(arr[1])

def parse_input(filename):
    file = open(f"{os.getcwd()}/13/{filename}", "r")
    arr = []

    pair = []

    for line in file:
        if len(pair) != 2:
            pair.append(line.strip())
        else:
            arr.append(pair)
            pair = []

    file.close()
    return arr

if __name__ == '__main__':
    main()
