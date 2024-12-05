import os

# Author: Cole Polyak
# 04 December 2024
# Advent of Code: Day 04

def main():
    arr = parse_input("day04.txt")
    search = list((list(s) for s in arr))

    horizontal = check_horizontal(search)
    vertical = check_vertical(search)
    diagonal = check_diagonal(search)

    print(f'Total valid XMAS-es: {horizontal + vertical + diagonal}')

def check_horizontal(search):
    count = 0
    for i in range(len(search)):
        for j in range(len(search[i])):
            try:
                snippet = search[i][j] + search[i][j + 1] + search[i][j + 2] + search[i][j + 3]
                if snippet == "XMAS" or snippet == "SAMX":
                    count += 1
            except:
                continue

    return count

def check_vertical(search):
    count = 0
    for i in range(len(search)):
        for j in range(len(search[i])):
            try:
                snippet = search[i][j] + search[i+ 1][j] + search[i + 2][j] + search[i + 3][j]
                if snippet == "XMAS" or snippet == "SAMX":
                    count += 1
            except:
                continue

    return count

def check_diagonal(search):
    count = 0
    for i in range(len(search)):
        for j in range(len(search[i])):
            try:
                snippets = []

                # Don't look at this, it's hideous.
                if not (i + 3 >= len(search) or j + 3 >= len(search[i])):
                    snippets.append(search[i][j] + search[i + 1][j + 1] + search[i + 2][j + 2] + search[i + 3][j + 3])
                
                if not (i - 3 < 0 or j + 3 >= len(search[i])):
                    snippets.append(search[i][j] + search[i - 1][j + 1] + search[i - 2][j + 2] + search[i - 3][j + 3])

                if not (i + 3 >= len(search) or j - 3 < 0):
                    snippets.append(search[i][j] + search[i + 1][j - 1] + search[i + 2][j - 2] + search[i + 3][j - 3])
                
                if not (i - 3 < 0 or j - 3 < 0):
                    snippets.append(search[i][j] + search[i - 1][j - 1] + search[i - 2][j - 2] + search[i - 3][j - 3])

                count += snippets.count("XMAS")

            except:
                continue

    return count

def parse_input(filename):
    file = open(f"{os.getcwd()}/04/{filename}", "r")
    arr = []

    for line in file:
        arr.append(line.strip())

    file.close()
    return arr

if __name__ == '__main__':
    main()
