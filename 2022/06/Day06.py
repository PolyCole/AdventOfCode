import os

# Author: Cole Polyak
# 06 December 2022
# Advent of Code: Day 06

def main():
    arr = parse_input("day06.txt")
    print(f"Part 1: {determine_signal(arr, 4)}")
    print(f"Part 2: {determine_signal(arr, 14)}")
    

def determine_signal(arr, window_size):
    window = []
    freq = {}

    count = 0
    
    for char in arr:
        if count < window_size:
            window.append(char)
            add_char_to_freq(char, freq)
            count += 1
            continue

        if chars_are_different(freq, window_size):
            return count
        
        count += 1
        removed = window.pop(0)
        window.append(char)
        add_char_to_freq(char, freq)
        remove_char_from_freq(removed, freq)
    
    return -1

def chars_are_different(freq, expected_size):
    return len(freq) == expected_size

def add_char_to_freq(char, freq):
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

def remove_char_from_freq(char, freq):
    if freq[char] == 1:
        freq.pop(char)
    else:
        freq[char] -= 1


def parse_input(filename):
    file = open(f"{os.getcwd()}/06/{filename}", "r")
    arr = []

    for line in file:
        return line.strip()

    return arr

if __name__ == '__main__':
    main()
