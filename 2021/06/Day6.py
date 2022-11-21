import os

# Author: Cole Polyak
# 6 December 2021
# Advent of Code: Day 6

# Works fine for small scale (pun intended), but isn't performant.
# class LanternFish:
#     def __init__(self, init_counter):
#         self.counter = init_counter
#
#     def count(self):
#         if self.counter == 0:
#             self.counter = 6
#             return True
#         else:
#             self.counter -= 1
#             return False
#
#     def __str__(self):
#         # return f"><(({self.counter}((o>"
#         return str(self.counter)


def main():
    arr = parse_input("day6.txt")

    # Instead, let's use an array to represent the 8 stages of a Lantern Fish.
    fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num in arr:
        fishes[int(num)] += 1

    for day in range(0, 256):        # day_num = f" {i + 1}" if i < 10 else i + 1
        new_fish = fishes[0]

        new_fish_states = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(1, len(fishes)):
            new_fish_states[i - 1] = fishes[i]

        new_fish_states
        new_fish_states[8] += new_fish
        new_fish_states[6] += new_fish
        fishes = new_fish_states
        print(f"Day {day} is over.")



    print(f"After 80 days, there are: {sum(fishes)} lantern fish.")



def parse_input(filename):
    file = open(f"{os.getcwd()}/{filename}", "r")
    return file.readline().strip().split(",")

if __name__ == '__main__':
    main()
