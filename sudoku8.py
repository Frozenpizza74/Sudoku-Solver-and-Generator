import numpy as np
import tkinter as tk
import random
from collections import deque

class Sudoku:
    def __init__(self, grid):
        self.grid = grid

    def is_valid(self, row, col, num):
        if num in self.grid[row] or num in self.grid[:, col]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        return num not in self.grid[start_row:start_row + 3, start_col:start_col + 3]

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i, j] == 0:
                    return i, j
        return None

    def backtrack_solve(self):
        empty = self.find_empty()
        if not empty: return True
        row, col = empty
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.grid[row, col] = num
                if self.backtrack_solve(): return True
                self.grid[row, col] = 0
        return False

    def bfs_solve(self):
        queue = deque([self.grid.copy()])
        while queue:
            current_grid = queue.popleft()
            if not Sudoku(current_grid).find_empty(): return True
            row, col = Sudoku(current_grid).find_empty()
            for num in range(1, 10):
                if self.is_valid(row, col, num):
                    new_grid = current_grid.copy()
                    new_grid[row, col] = num
                    queue.append(new_grid)
        return False

class SudokuApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sudoku Solver")
        self.entries = [[tk.Entry(self.window, width=3, justify='center') for _ in range(9)] for _ in range(9)]
        for i, row in enumerate(self.entries):
            for j, cell in enumerate(row):
                cell.grid(row=i, column=j, padx=1, pady=1)
        tk.Button(self.window, text="Generate", command=self.generate).grid(row=10, column=0, columnspan=4)
        tk.Button(self.window, text="Solve (CSP)", command=self.solve).grid(row=10, column=4, columnspan=4)
        tk.Button(self.window, text="Solve (DFS)", command=self.solve_dfs).grid(row=10, column=8, columnspan=4)
        tk.Button(self.window, text="Solve (BFS)", command=self.solve_bfs).grid(row=11, column=4, columnspan=8)

    def generate(self):
        puzzle = self.generate_sudoku()
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if puzzle[i, j] != 0:
                    self.entries[i][j].insert(0, puzzle[i, j])

    def get_grid(self):
        return np.array([[int(cell.get()) if cell.get() else 0 for cell in row] for row in self.entries])

    def update_grid(self, grid):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, grid[i, j])

    def solve(self):
        sudoku = Sudoku(self.get_grid())
        if sudoku.backtrack_solve():
            self.update_grid(sudoku.grid)

    def solve_dfs(self):
        sudoku = Sudoku(self.get_grid())
        if sudoku.backtrack_solve():
            self.update_grid(sudoku.grid)

    def solve_bfs(self):
        sudoku = Sudoku(self.get_grid())
        if sudoku.bfs_solve():
            self.update_grid(sudoku.grid)

    def generate_sudoku(self):
        base = np.array([[(i * 3 + i // 3 + j) % 9 + 1 for j in range(9)] for i in range(9)])
        for _ in range(30):
            a, b = divmod(random.randint(0, 8), 3)
            row1, row2 = random.sample(range(a * 3, (a + 1) * 3), 2)
            base[[row1, row2]] = base[[row2, row1]]
            col1, col2 = random.sample(range(b * 3, (b + 1) * 3), 2)
            base[:, [col1, col2]] = base[:, [col2, col1]]
        puzzle = base.copy()
        for _ in range(40):
            puzzle[random.randint(0, 8), random.randint(0, 8)] = 0
        return puzzle

    def run(self):
        self.window.mainloop()

SudokuApp().run()
