import os

# Author: Cole Polyak
# 02 December 2024
# Advent of Code: Day 02

def main():
    arr = parse_input("day02.txt")

    count = 0

    for line in arr:
        split = line.split(" ")
        split = list(map(int, split))
        count += calculate_safe(split)
        
    print(count)

def calculate_safe(arr, depth=0):   
    prev = arr[0]

    # 0 -- neutral
    # 1 -- increasing
    # 2 -- decreasing
    is_increasing = 0
    for i in range(1, len(arr)):
        if prev - arr[i] <= 3 and prev - arr[i] > 0:
            if is_increasing == 0 or is_increasing == 1:
                is_increasing = 1
                prev = arr[i]
            else:
                if depth == 0:
                    return check_recursive(arr)
                else:
                    return 0
        elif prev - arr[i] >= -3 and prev - arr[i] < 0:
            if is_increasing == 0 or is_increasing == 2:
                is_increasing = 2
                prev = arr[i]
            else:
                if depth == 0:
                    return check_recursive(arr)
                else:
                    return 0
        else:
            if depth == 0:
                return check_recursive(arr)
            else:
                return 0
    return 1

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
