'''
Implement a solution for a Constraint Satisfaction Problem using Branch and Bound for
n-queens problem.
'''
def solve_n_queens(n):
    """
    Solve the n-queens problem using recursive branch-and-bound (backtracking with pruning).
    Returns a list of solutions. Each solution is a list of column indices;
    solution[row] = column where a queen is placed in that row.
    """
    solutions = []           # will collect all valid solutions
    cols = set()             # columns that are already occupied
    diag1 = set()            # r - c for occupied major diagonals
    diag2 = set()            # r + c for occupied minor diagonals
    partial = []             # partial solution: list of columns for rows 0..row-1

    def place(row):
        # If we've placed queens on all rows, record the solution
        if row == n:
            solutions.append(partial.copy())
            return

        # Try every column in this row
        for c in range(n):
            # Bound: skip if column or diagonals are already attacked
            if c in cols or (row - c) in diag1 or (row + c) in diag2:
                continue

            # Choose: place queen at (row, c)
            cols.add(c)
            diag1.add(row - c)
            diag2.add(row + c)
            partial.append(c)

            # Recurse to next row
            place(row + 1)

            # Unchoose (backtrack): remove the queen and try next column
            partial.pop()
            cols.remove(c)
            diag1.remove(row - c)
            diag2.remove(row + c)

    # Start recursion from row 0
    place(0)
    return solutions


# Example usage: print all solutions for n = 4
if __name__ == "__main__":
    n = 4
    sols = solve_n_queens(n)
    print(f"Number of solutions for n={n}: {len(sols)}")
    for sol in sols:
        print(sol)
