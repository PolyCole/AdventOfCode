import os

# Author: Cole Polyak
# 4 December 2021
# Advent of Code: Day 4

class BingoBoard:
    def __init__(self):
        # We need the 2D array for the board representation, but lookups on 2D
        # arrays are #garbage, so we'll construct a lookup set.
        self.lookup = set()
        self.board = []

    def add_row(self, nums):
        new_row = []

        for num in nums:
            num = int(num)
            self.lookup.add(num)
            new_row.append((num, False))

        self.board.append(new_row)

    def mark_number(self, target_num):
        if target_num in self.lookup:
            for row in range(0, len(self.board)):
                for square in range(0, len(self.board[row])):
                    num, marked = self.board[row][square]

                    if num == int(target_num):
                        self.board[row][square] = (num, True)
                        return True
        return False

    def has_bingo(self):

        # Check rows
        for row in self.board:
            bingo = True
            for num, marked in row:
                bingo = bingo and marked
            if bingo:
                return True

        # Check Columns
        for i in range(0, len(self.board)):
            bingo = True
            for j in range(0, len(self.board[i])):
                num, marked = self.board[j][i]
                bingo = bingo and marked
            if bingo:
                return True
        return False

    def calculate_score(self, number_called):
        sum = 0
        for row in self.board:
            for num, marked in row:
                if marked == False:
                    sum += int(num)
                    print(f"***{num}***")

        print(f"Sum: {sum}, Number called: {number_called}, product: {sum * int(number_called)}")
        return sum * int(number_called)



    def __str__(self):
        # I know there are more efficient ways of generating strings in python,
        # but that's not the main focus of this problem, so I'm going to leave this.
        output = ""

        for row in self.board:
            output += "\n"
            for num, marked in row:
                if num < 10:
                    output += " "
                is_marked = "x" if marked else " "
                output += f"{num} ({is_marked}) "

        return output


def main():
    nums, boards = parse_input("day4.txt")

    # Part 1
    # for called_number in nums:
    #     print(f"CALLING: {called_number}")
    #
    #     # first, mark all boards.
    #     for board in boards:
    #         board.mark_number(called_number)
    #
    #         # second, check for bingo.
    #         if board.has_bingo():
    #             board.calculate_score(called_number)
    #             print(f"{board}")
    #             return

    # Part 2
    for called_number in nums:
        print(f"\nCALLING: {called_number}")
        no_bingo = []
        for i in range(0, len(boards)):
            board = boards[i]

            board.mark_number(called_number)

            # second, check for bingo.
            if board.has_bingo() == False:
                print(f"BEEP")
                no_bingo.append(board)
            else:
                if len(boards) == 1:
                    print(f"Haha Loser board loser board")
                    boards[0].calculate_score(called_number)
                    print(f"{boards[0]}")
                    return

        boards = no_bingo



def parse_input(filename):
    file = open(f"{os.getcwd()}/{filename}", "r")

    nums = list(map(lambda x: int(x), file.readline().strip().split(",")))

    previous_line = list(filter(lambda x: x != '', file.readline().strip().split(" ")))
    current_line = list(filter(lambda x: x != '', file.readline().strip().split(" ")))

    boards = []
    current_board = BingoBoard()

    while(previous_line != [] or current_line != []):
        # Just finished reading a board.
        if current_line == []:
            previous_line == current_line
            boards.append(current_board)
            current_board = BingoBoard()
            current_line = file.readline().strip().split(" ")
            current_line = list(filter(lambda x: x != '', current_line))


        current_board.add_row(current_line)
        previous_line = current_line
        current_line = file.readline().strip().split(" ")
        current_line = list(filter(lambda x: x != '', current_line))

    return nums, boards

if __name__ == '__main__':
    main()
