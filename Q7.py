'''Implement a solution for a Constraint Satisfaction Problem using Backtracking for
graph coloring problem.'''
# Simple backtracking graph coloring (k-coloring decision + finder)

def can_color_with_k(graph, k):
    """
    Try to color 'graph' with k colors using backtracking.
    graph: adjacency list as list of lists, vertices are 0..n-1
    k: number of colors (colors are 0..k-1)
    Returns: list of colors if successful, or None if no coloring exists with k colors.
    """
    n = len(graph)
    colors = [-1] * n  # -1 means unassigned

    def safe(vertex, c):
        """Return True if no neighbor of 'vertex' already has color c."""
        for neigh in graph[vertex]:
            if colors[neigh] == c:
                return False
        return True

    def assign(v):
        """Try to color vertex v and onward. Returns True if success."""
        if v == n:               # all vertices colored
            return True
        for c in range(k):       # try each color
            if safe(v, c):
                colors[v] = c
                if assign(v + 1):  # recurse
                    return True
                colors[v] = -1     # backtrack
        return False

    if assign(0):
        return colors
    return None


def find_smallest_coloring(graph):
    """
    Naively try k = 1..n and return the first successful coloring and k.
    This gives a valid coloring with the smallest k found by brute force.
    """
    n = len(graph)
    for k in range(1, n + 1):
        result = can_color_with_k(graph, k)
        if result is not None:
            return k, result
    return None, None


# Example usage
if __name__ == "__main__":
    # Example 1: triangle (3 vertices all connected) -> needs 3 colors
    triangle = [
        [1, 2],  # neighbors of vertex 0
        [0, 2],  # vertex 1
        [0, 1]   # vertex 2
    ]
    k, coloring = find_smallest_coloring(triangle)
    print("Triangle -> smallest k:", k, "coloring:", coloring)

    # Example 2: square (cycle of 4) -> needs 2 colors
    square = [
        [1, 3],  # 0
        [0, 2],  # 1
        [1, 3],  # 2
        [0, 2]   # 3
    ]
    k2, coloring2 = find_smallest_coloring(square)
    print("Square -> smallest k:", k2, "coloring:", coloring2)
