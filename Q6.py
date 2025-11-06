'''6)Implement a solution for a Constraint Satisfaction Problem using Branch and Bound for
graph coloring problem.'''

# Very simple Branch-and-Bound graph coloring (minimize colors)
# Graph is adjacency list: graph[v] -> list of neighbor vertices

def graph_coloring_branch_and_bound(graph):
    n = len(graph)

    # 1) quick greedy coloring to get an initial upper bound
    def greedy_order_coloring(order):
        color = [-1] * n
        for v in order:
            forbidden = {color[u] for u in graph[v] if color[u] != -1}
            # choose smallest color not forbidden
            c = 0
            while c in forbidden:
                c += 1
            color[v] = c
        used = max(color) + 1
        return used, color

    # order vertices by descending degree (helps pruning)
    initial_order = sorted(range(n), key=lambda x: -len(graph[x]))
    ub_used, ub_assignment = greedy_order_coloring(initial_order)  # upper bound

    best_colors = ub_used
    best_assignment = ub_assignment.copy()

    # 2) prepare search order and structures
    order = initial_order  # we color vertices in this order
    assignment = [-1] * n

    # helper: check if vertex v can take color c under current assignment
    def can_color(v, c):
        for nei in graph[v]:
            if assignment[nei] == c:
                return False
        return True

    # 3) recursive search with branch-and-bound
    def search(idx, used):
        nonlocal best_colors, best_assignment
        if used >= best_colors:
            # bound: already used too many colors -> prune
            return

        if idx == n:
            # a full coloring found with 'used' colors -> update best
            best_colors = used
            best_assignment = assignment.copy()
            return

        v = order[idx]

        # try existing colors 0..used-1
        for c in range(used):
            if can_color(v, c):
                assignment[v] = c
                search(idx + 1, used)
                assignment[v] = -1

        # try a new color 'used' (increase colors by 1) if it can improve best
        if used + 1 < best_colors:
            assignment[v] = used
            search(idx + 1, used + 1)
            assignment[v] = -1

    # start search
    search(0, 0)
    return best_colors, best_assignment


# ---------- Example usage ----------
if __name__ == "__main__":
    # Example graph (triangle plus an extra node):
    # 0--1
    #  \ |
    #    2
    # 3 is isolated
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1],
        3: []
    }
    # convert to list-of-lists (index must be 0..n-1)
    n = max(graph.keys()) + 1
    adj = [graph[i] for i in range(n)]

    colors_used, assignment = graph_coloring_branch_and_bound(adj)
    print("Minimum colors found:", colors_used)
    print("Color per vertex (vertex:color):", list(enumerate(assignment)))
