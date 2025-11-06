'''Implement Greedy search algorithm for Kruskal's Minimal Spanning Tree Algorithm'''

# Kruskal's algorithm (simple, easy-to-read)
# Graph is given as a list of edges: (u, v, weight)
# Vertices can be integers or any hashable objects.

def kruskal(edges):
    """
    edges: list of tuples (u, v, w)
    returns: (mst_edges, total_cost)
      mst_edges: list of (u, v, w) that form the MST
      total_cost: sum of weights in the MST
    """

    # 1. Make a list of unique vertices
    verts = set()
    for u, v, _ in edges:
        verts.add(u)
        verts.add(v)
    verts = list(verts)

    # 2. Disjoint Set Union (Union-Find) helper implementation
    parent = {v: v for v in verts}   # parent pointer for each vertex
    rank = {v: 0 for v in verts}     # rank (approximate tree height)

    def find(x):
        # find root with path compression
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # path compression step (point to grandparent)
            x = parent[x]
        return x

    def union(a, b):
        # union by rank
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False  # already in same set; union did not happen
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[rb] < rank[ra]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1
        return True

    # 3. Sort edges by weight
    edges_sorted = sorted(edges, key=lambda e: e[2])

    # 4. Kruskal main loop
    mst_edges = []
    total_cost = 0

    for u, v, w in edges_sorted:
        if union(u, v):           # if u and v were in different components
            mst_edges.append((u, v, w))
            total_cost += w

        # optional small optimization: stop when we have len(verts)-1 edges
        if len(mst_edges) == len(verts) - 1:
            break

    return mst_edges, total_cost


# ---------- Example usage ----------
if __name__ == "__main__":
    # Example undirected weighted graph as edge list
    # (u, v, weight) — since graph is undirected, provide each edge once
    example_edges = [
        (0, 1, 4),
        (0, 7, 8),
        (1, 7, 11),
        (1, 2, 8),
        (7, 8, 7),
        (7, 6, 1),
        (2, 8, 2),
        (8, 6, 6),
        (2, 3, 7),
        (2, 5, 4),
        (6, 5, 2),
        (3, 5, 14),
        (3, 4, 9),
        (4, 5, 10)
    ]

    mst, cost = kruskal(example_edges)
    print("MST edges:")
    for u, v, w in mst:
        print(f"  {u} -- {v}  (weight {w})")
    print("Total MST cost:", cost)
