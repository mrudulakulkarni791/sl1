# Simple recursive DFS for an undirected graph (adjacency list)

def dfs_recursive(graph, start, visited=None, result=None):
    """
    Perform a recursive depth-first search starting from `start`.
    graph: dict where keys are vertices and values are lists of neighbors
    start: vertex to begin DFS from
    visited: set used to track visited vertices (internal use)
    result: list used to collect traversal order (internal use)
    Returns: list of vertices in the order they were visited
    """
    if visited is None:
        visited = set()
    if result is None:
        result = []

    # Mark start visited and record it
    visited.add(start)
    result.append(start)

    # Recurse on unvisited neighbors
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)

    return result


# Example usage:
if __name__ == "__main__":
    # Undirected graph as adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
        # a disconnected node
        'G': []
    }

    # Start DFS from 'A'
    traversal_from_A = dfs_recursive(graph, 'A')
    print("DFS starting from A:", traversal_from_A)

    # To traverse whole graph including disconnected components:
    visited = set()
    full_order = []
    for vertex in graph:
        if vertex not in visited:
            # call dfs_recursive but share visited & result to accumulate
            dfs_recursive(graph, vertex, visited, full_order)

    print("Full DFS order for all components:", full_order)
