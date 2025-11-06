'''Implement A star (A*) Algorithm for any game search problem.'''
# Simple A* algorithm on a grid (easy to understand)

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = [start]      # nodes to visit
    came_from = {}           # to reconstruct path
    g = {start: 0}           # cost from start
    f = {start: heuristic(start, goal)}  # total estimated cost

    while open_list:
        # Pick node with smallest f value
        current = min(open_list, key=lambda x: f.get(x, float('inf')))
        
        # Goal reached
        if current == goal:
            return reconstruct_path(came_from, current)
        
        open_list.remove(current)
        r, c = current

        # Check 4-directional neighbors
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)

            # Skip invalid or blocked cells
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if grid[nr][nc] == 1:
                continue

            # Cost from start to neighbor
            tentative_g = g[current] + 1

            if tentative_g < g.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g[neighbor] = tentative_g
                f[neighbor] = tentative_g + heuristic(neighbor, goal)
                if neighbor not in open_list:
                    open_list.append(neighbor)

    return None  # no path found


def heuristic(a, b):
    # Manhattan distance (works for 4-direction grid)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


# Example usage
if __name__ == "__main__":
    # 0 = free cell, 1 = obstacle
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    start = (0, 0)
    goal = (4, 4)

    path = a_star(grid, start, goal)
    if path:
        print("Path found:", path)
    else:
        print("No path found.")
