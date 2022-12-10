import os

# Author: Cole Polyak
# 02 December 2022
# Advent of Code: Day 02

# Elf's moves
elfs_moves = {
    "A": "Rock",
    "B": "Paper", 
    "C": "Scissors"
}

# Score of Move
score = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

def main():
    arr = parse_input("day02.txt")

    # O(n) algorithmic
    # O(1) spacial

    part1(arr)
    part2(arr)
    

def part1(arr):
    # Me
    my_moves = {
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors"
    }

    total_score = 0

    for turn in arr:
        elf, me = turn

        elfs_move = elfs_moves[elf]
        my_move = my_moves[me]

        if elfs_move == my_move:
            total_score += round_result_points("Draw")
        elif i_win_round(elfs_move, my_move):
            total_score += round_result_points("Win")
        
        total_score += move_points(my_move)
    
    print(f"\n\nPart 1 Output")
    print(f"Total score: {total_score}\n\n")

def part2(arr):
    need = {
        "X": "Lose",
        "Y": "Draw",
        "Z": "Win"
    }

    total_score = 0

    for turn in arr:
        elf_move, outcome = turn

        elfs_move = elfs_moves[elf_move]
        desired_outcome = need[outcome]

        # Tie
        if desired_outcome == "Draw":
            total_score += move_points(elfs_move)
        # I win
        elif desired_outcome == "Win":
            total_score += winning_move_points(elfs_move)
        # I lose
        else:
            total_score += losing_move_points(elfs_move)

        total_score += round_result_points(desired_outcome)

    print(f"Part 2 Output")
    print(f"Total score: {total_score}")

def round_result_points(result):
    if result == "Win":
        return 6
    elif result == "Draw":
        return 3
    else:
        # Lose
        return 0

def move_points(move):
    return score[move]

def i_win_round(elfs_move, my_move):
    # K -- What my move is
    # V -- What move beats my move.
    move_i_lose_to = {
        "Paper": "Rock",
        "Rock": "Scissors", 
        "Scissors": "Paper"
    }

    return move_i_lose_to[my_move] == elfs_move

def winning_move_points(elf):
    # K -- Elf's Move
    # V -- What I need to play to win.
    win = {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock"
    }

    return score[win[elf]]

def losing_move_points(elf):
    # K -- Elf's Move
    # V -- What I need to play to lose.
    lose = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }

    return score[lose[elf]]


def parse_input(filename):
    file = open(f"{os.getcwd()}/02/{filename}", "r")
    arr = []

    # Storing each term as a tuple with my move and the elf's move.
    for line in file:
        arr.append((line.strip().split(" ")))

    file.close()
    return arr

if __name__ == '__main__':
    main()
