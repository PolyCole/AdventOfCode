import os

# Author: Cole Polyak
# XX December 2024
# Advent of Code: Day XX

def main():
    arr = parse_input("dayXX.txt")

def parse_input(filename):
    file = open(f"{os.getcwd()}/XX/{filename}", "r")
    arr = []

    for line in file:
        arr.append(line.strip())

    file.close()
    return arr

if __name__ == '__main__':
    main()
