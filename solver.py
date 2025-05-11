class SudokuSolver:
    def __init__(self, board):
        self.board = board
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]
        self.empty_cells = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != 0:
                    self.rows[r].add(val)
                    self.cols[c].add(val)
                    self.boxes[self.get_box_index(r, c)].add(val)
                else:
                    self.empty_cells.append((r, c))

    def get_box_index(self, row, col):
        return (row // 3) * 3 + (col // 3)

    def is_valid(self, row, col, num):
        box = self.get_box_index(row, col)
        return (num not in self.rows[row] and
                num not in self.cols[col] and
                num not in self.boxes[box])

    def place_number(self, row, col, num):
        self.board[row][col] = num
        self.rows[row].add(num)
        self.cols[col].add(num)
        self.boxes[self.get_box_index(row, col)].add(num)

    def remove_number(self, row, col, num):
        self.board[row][col] = 0
        self.rows[row].remove(num)
        self.cols[col].remove(num)
        self.boxes[self.get_box_index(row, col)].remove(num)

    def solve(self, index=0):
        if index == len(self.empty_cells):
            return True

        row, col = self.empty_cells[index]
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.place_number(row, col, num)

                if self.solve(index + 1):
                    return True

                self.remove_number(row, col, num)

        return False

    def print_board(self):
        for i, row in enumerate(self.board):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j, num in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(num if num != 0 else ".", end=" ")
            print()

def get_user_input():
    print("Enter your Sudoku puzzle row by row (use 0 for empty cells):")
    board = []
    for i in range(9):
        while True:
            row = input(f"Row {i + 1}: ")
            if len(row) == 9 and all(ch.isdigit() for ch in row):
                board.append([int(ch) for ch in row])
                break
            else:
                print("Invalid input. Please enter exactly 9 digits (0-9).")
    return board

# Main
board = get_user_input()
solver = SudokuSolver(board)

print("\nOriginal Sudoku Puzzle:")
solver.print_board()

if solver.solve():
    print("\nSolved Sudoku Puzzle:")
    solver.print_board()
else:
    print("No solution exists.")
