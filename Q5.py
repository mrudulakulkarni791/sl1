def solve_n_queens(n):
    """
Implement a solution for a Constraint Satisfaction Problem using Backtracking for nqueens problem.

    Solve n-queens with backtracking.
    Returns a list of solutions; each solution is a list of column indices:
      solution[row] = column where the queen is placed in that row.
    """
    solutions = []
    cols = set()      # columns that already have a queen
    diag1 = set()     # row - col for occupied major diagonals
    diag2 = set()     # row + col for occupied minor diagonals
    partial = []      # partial solution: columns for rows 0..row-1

    def place(row):
        # If all rows are filled, record the solution
        if row == n:
            solutions.append(partial.copy())
            return

        # Try every column in this row
        for c in range(n):
            # If placing at (row, c) conflicts, skip it
            if c in cols or (row - c) in diag1 or (row + c) in diag2:
                continue

            # Place queen at (row, c)
            cols.add(c)
            diag1.add(row - c)
            diag2.add(row + c)
            partial.append(c)

            # Recurse to next row
            place(row + 1)

            # Backtrack: remove queen and try next column
            partial.pop()
            cols.remove(c)
            diag1.remove(row - c)
            diag2.remove(row + c)

    # Start from row 0
    place(0)
    return solutions


def print_board(solution):
    """Helper to print one solution in a human-friendly board format."""
    n = len(solution)
    for r in range(n):
        row = ['.'] * n
        row[solution[r]] = 'Q'
        print(' '.join(row))
    print()


# Example usage
if __name__ == "__main__":
    n = 4
    sols = solve_n_queens(n)
    print(f"Found {len(sols)} solutions for n = {n}\n")
    for s in sols:
        print_board(s)
