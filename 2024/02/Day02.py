import os

# Author: Cole Polyak
# 02 December 2024
# Advent of Code: Day 02

def main():
    global PART
    PART = 1
    arr = parse_input("day02.txt")
    execute(arr.copy())
    PART = 2
    execute(arr.copy())

def execute(arr):
    count = 0

    for line in arr:
        split = line.split(" ")
        split = list(map(int, split))
        count += calculate_safe(split)
        
    print(f'PART {PART} ANSWER: {count}')

def calculate_safe(arr, depth=0):   
    prev = arr[0]

    # 0 -- neutral
    # 1 -- decreasing
    # 2 -- increasing
    is_increasing = 0
    for i in range(1, len(arr)):
        diff = prev - arr[i]
        # Previous > Current == Increasing in range.
        if diff <= 3 and diff > 0:
            # We're not already decreasing.
            if is_increasing != 2:
                is_increasing = 1
                prev = arr[i]
            else:
                return check_fail_case(arr, depth)
        # Previous < Current = Decreasing in range.
        elif diff >= -3 and diff < 0:
            # We're not already increasing.
            if is_increasing != 1:
                is_increasing = 2
                prev = arr[i]
            else:
                return check_fail_case(arr, depth)
        # Difference is outside of acceptable range.
        else:
            return check_fail_case(arr, depth)
    return 1

# Checks if we should recurse or not, now that we've found an unsafe path.
def check_fail_case(arr, depth):
    if PART == 2 and depth == 0:
        return check_recursive(arr)
    else:
        return 0

# Recursively checks if we can remove a number and have a safe path.
def check_recursive(arr):
    for i in range(0, len(arr)):
        temp = arr.copy()
        del temp[i]

        result = calculate_safe(temp, 1)
        if result == 1:
            return 1
    
    return 0

def parse_input(filename):
    file = open(f"{os.getcwd()}/02/{filename}", "r")
    arr = []

    for line in file:
        arr.append(line.strip())

    file.close()
    return arr

if __name__ == '__main__':
    main()
