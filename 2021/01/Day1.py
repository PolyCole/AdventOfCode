import os

# Author: Cole Polyak
# 1 December 2021
# Advent of Code: Day 1

def main():
    arr = parse_input("day1.txt")
    check_increases_in_window(arr, 1, "\n*****\nPart 1 Answer:")
    check_increases_in_window(arr, 3, "\n*****\nPart 2 Answer:")

# Counts the number of increases in the provided window size.
def check_increases_in_window(arr, window_size, fluff):
    increases = 0
    previous_window = arr[0]

    # Simplified it's O(n)
    for i in range(1, len(arr)):
        if i == len(arr) - (window_size - 1):
            break

        current_window = sum(arr[i:(i + window_size)])

        if current_window > previous_window:
            increases += 1

        previous_window = current_window

    final_output(increases, fluff)

def final_output(increases, fluff):
    print(fluff)
    print(f"I think it increased {increases} times.")
    print("*****\n")

def parse_input(filename):
    file = open(f"{os.getcwd()}/{filename}", "r")
    arr = []
    
    for line in file:
        arr.append(int(line.strip()))
    file.close()
    return arr

if __name__ == '__main__':
    main()
