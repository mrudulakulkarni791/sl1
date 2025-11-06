# Recursive BFS for an undirected graph (adjacency list)

def bfs_recursive_from_start(graph, start):
    """
    Perform BFS starting from `start` using a recursive, level-by-level approach.
    graph: dict where keys are vertices and values are lists of neighbors
    start: starting vertex
    Returns: list of vertices in BFS order reachable from start
    """
    visited = set()
    result = []

    # Helper: process one level and recurse on the next level
    def bfs_level(current_level):
        if not current_level:
            return  # base case: no more levels to process

        # Mark nodes in this level as visited and record them
        for node in current_level:
            if node not in visited:
                visited.add(node)
                result.append(node)

        # Build the next level: neighbors of current level not yet visited
        next_level = []
        for node in current_level:
            for neighbor in graph.get(node, []):
                if neighbor not in visited and neighbor not in next_level:
                    next_level.append(neighbor)

        # Recurse to process the next level
        bfs_level(next_level)

    # Start recursion with the starting node (use list even if node absent in graph)
    bfs_level([start])
    return result


def bfs_recursive_full(graph):
    """
    Perform BFS for the whole graph, covering disconnected components.
    Returns: list of vertices in the order they were visited (component by component)
    """
    visited = set()
    full_result = []

    for vertex in graph:
        if vertex not in visited:
            # Use the same level-based recursion but share visited/full_result
            def bfs_level_shared(current_level):
                if not current_level:
                    return
                for node in current_level:
                    if node not in visited:
                        visited.add(node)
                        full_result.append(node)
                next_level = []
                for node in current_level:
                    for neighbor in graph.get(node, []):
                        if neighbor not in visited and neighbor not in next_level:
                            next_level.append(neighbor)
                bfs_level_shared(next_level)

            bfs_level_shared([vertex])

    return full_result


# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
        'G': []  # disconnected node
    }

    print("BFS from A:", bfs_recursive_from_start(graph, 'A'))
    print("Full BFS over all components:", bfs_recursive_full(graph))
