import os

# Author: Cole Polyak
# X December 2021
# Advent of Code: Day X

def main():
    arr = parse_input("dayX.txt")

def parse_input(filename):
    file = open(f"{os.getcwd()}/{filename}", "r")
    arr = []

    for line in file:
        arr.append(line.strip())

    return arr

if __name__ == '__main__':
    main()
