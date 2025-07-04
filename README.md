# Sudoku-Solver-and-Generator
This Python project implements a Sudoku puzzle solver and generator with a graphical user interface (GUI) using Tkinter. It features multiple solving algorithms and puzzle generation capabilities.
----------------------------------------------------------------
GUI Controls:
Generate Button: Creates a new Sudoku puzzle

Solve (CSP): Solves using backtracking algorithm (recommended)

Solve (DFS): Solves using depth-first search

Solve (BFS): Solves using breadth-first search

Manual Input: Type numbers directly into the grid (use 0 or leave blank for empty cells)

Example Workflow:
Click "Generate" to create a new puzzle

Modify cells manually if desired

Click any solve button to see the solution

Generate new puzzles to try different challenges

Implementation Details
Uses NumPy for grid operations

Backtracking solver is most efficient for typical Sudoku puzzles

BFS implementation shows alternative solving approach

Puzzle generation starts with valid solution and removes clues

GUI provides real-time feedback and updates

Notes
BFS may be slow for complex puzzles due to memory requirements

Backtracking (CSP) is generally the fastest solver

Default puzzle difficulty can be adjusted by modifying clue removal count in code
