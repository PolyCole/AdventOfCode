import os

# Author: Cole Polyak
# 04 December 2024
# Advent of Code: Day 04

def main():
    arr = parse_input("day04.txt")
    search = list((list(s) for s in arr))

    diagonal = check_diagonal(search)

    print(f'Total valid X-MASes: {diagonal}')


def check_diagonal(search):
    count = 0
    for i in range(len(search)):
        for j in range(len(search[i])):
            try:
                snippets = []
                
                # Don't look at this either, it's hideous.
                if not (i + 1 >= len(search) or j + 1 >= len(search[i])) and not (i - 1 < 0 or j - 1 < 0):
                    snippets.append(search[i-1][j-1] + search[i][j] + search[i+1][j+1])
                    snippets.append(search[i-1][j+1] + search[i][j] + search[i+1][j-1])

                good_count = 0
                for snippet in snippets:
                    if snippet == "MAS" or snippet == "SAM":
                        good_count += 1

                if(good_count == 2):
                    count += 1

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
