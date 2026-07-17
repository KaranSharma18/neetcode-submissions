from collections import defaultdict, deque
from typing import List, Optional


# ═══════════════════════════════════════════════════════════════════
# 1. GRAPH REPRESENTATIONS
# ═══════════════════════════════════════════════════════════════════

# Adjacency list — the standard for interview problems
# O(V + E) space, O(degree) neighbor lookup

def build_undirected(n: int, edges: List[List[int]]) -> defaultdict:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)   # both directions
    return graph

def build_directed(n: int, edges: List[List[int]]) -> defaultdict:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)   # one direction only
    return graph

# Adjacency matrix — use when you need O(1) edge existence check
# O(V²) space — only practical for dense graphs or small V

def build_matrix(n: int, edges: List[List[int]]) -> List[List[int]]:
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1     # undirected
    return matrix


# ═══════════════════════════════════════════════════════════════════
# 2. BFS — BREADTH FIRST SEARCH
# ═══════════════════════════════════════════════════════════════════
# Use for: shortest path in unweighted graph, level-by-level traversal
# Time: O(V + E)  Space: O(V)

def bfs(graph: dict, start: int) -> List[int]:
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()    # FIFO — deque not list (popleft is O(1))
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


# BFS shortest path — returns distance from start to end, -1 if unreachable
def bfs_shortest_path(graph: dict, start: int, end: int) -> int:
    if start == end:
        return 0

    visited = {start}
    queue = deque([(start, 0)])    # (node, distance)

    while queue:
        node, dist = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == end:
                return dist + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1    # no path


# ═══════════════════════════════════════════════════════════════════
# 3. DFS — DEPTH FIRST SEARCH
# ═══════════════════════════════════════════════════════════════════
# Use for: connectivity, path existence, cycle detection, topo sort
# Time: O(V + E)  Space: O(V) recursion stack

# Recursive DFS — cleaner, most common in interviews
def dfs_recursive(graph: dict, node: int, visited: set) -> None:
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Iterative DFS — avoids recursion limit for large graphs
def dfs_iterative(graph: dict, start: int) -> List[int]:
    visited = {start}
    stack = [start]
    order = []

    while stack:
        node = stack.pop()    # LIFO — this is the key difference from BFS
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return order


# ═══════════════════════════════════════════════════════════════════
# 4. CONNECTED COMPONENTS
# ═══════════════════════════════════════════════════════════════════
# Count how many disconnected subgraphs exist
# Time: O(V + E)  Space: O(V)

def count_components(n: int, edges: List[List[int]]) -> int:
    graph = build_undirected(n, edges)
    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in range(n):
        if node not in visited:
            dfs(node)
            count += 1        # each new DFS call from outer loop = new component

    return count


# ═══════════════════════════════════════════════════════════════════
# 5. CYCLE DETECTION
# ═══════════════════════════════════════════════════════════════════

# UNDIRECTED: a cycle exists if DFS visits an already-visited node
# that isn't the node we came from (the parent)
# Time: O(V + E)  Space: O(V)

def has_cycle_undirected(n: int, edges: List[List[int]]) -> bool:
    graph = build_undirected(n, edges)
    visited = set()

    def dfs(node, parent) -> bool:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:    # visited AND not parent = back edge = cycle
                return True
        return False

    for node in range(n):
        if node not in visited:
            if dfs(node, -1):
                return True
    return False


# DIRECTED: a cycle exists if DFS finds a "back edge" —
# a neighbor that's currently in the active DFS path (gray/in-progress)
# Time: O(V + E)  Space: O(V)

def has_cycle_directed(n: int, edges: List[List[int]]) -> bool:
    graph = build_directed(n, edges)

    WHITE, GRAY, BLACK = 0, 1, 2    # unvisited, in-progress, fully done
    color = [WHITE] * n

    def dfs(node) -> bool:
        color[node] = GRAY            # mark as currently exploring
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:     # back edge — cycle found
                return True
            if color[neighbor] == WHITE:    # unvisited — explore it
                if dfs(neighbor):
                    return True
        color[node] = BLACK           # all neighbors done — safe to leave
        return False

    for node in range(n):
        if color[node] == WHITE:
            if dfs(node):
                return True
    return False


# ═══════════════════════════════════════════════════════════════════
# 6. TOPOLOGICAL SORT
# ═══════════════════════════════════════════════════════════════════
# Only valid for DAGs (directed acyclic graphs)
# Produces an ordering where every node comes before its dependencies

# BFS approach (Kahn's algorithm) — preferred in interviews
# Key idea: nodes with in-degree 0 have no prerequisites → process first
# Time: O(V + E)  Space: O(V)

def topological_sort_bfs(n: int, edges: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    in_degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1            # v has one more prerequisite

    queue = deque()
    for node in range(n):
        if in_degree[node] == 0:     # no prerequisites — safe to start here
            queue.append(node)

    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:    # all its prerequisites done
                queue.append(neighbor)

    # If order doesn't contain all nodes, a cycle exists (Course Schedule pattern)
    return order if len(order) == n else []


# DFS approach — push to stack AFTER all neighbors are processed
# Reverse of the stack gives topological order
# Time: O(V + E)  Space: O(V)

def topological_sort_dfs(n: int, edges: List[List[int]]) -> List[int]:
    graph = build_directed(n, edges)
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)            # pushed AFTER all descendants — key line

    for node in range(n):
        if node not in visited:
            dfs(node)

    return stack[::-1]               # reverse gives correct order


# ═══════════════════════════════════════════════════════════════════
# 7. UNION-FIND (DISJOINT SET UNION)
# ═══════════════════════════════════════════════════════════════════
# Best for: detecting cycles, counting connected components
# find and union are effectively O(1) amortised with both optimisations

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))  # each node is its own parent initially
        self.rank = [0] * n           # tree height estimate — keeps trees flat
        self.components = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False              # already in the same component
                                      # adding this edge would create a cycle
        if self.rank[px] < self.rank[py]:
            px, py = py, px           # always attach smaller tree under larger
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True                   # successfully merged two components

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


# ═══════════════════════════════════════════════════════════════════
# 8. GRID AS A GRAPH — THE ISLAND PATTERN
# ═══════════════════════════════════════════════════════════════════
# Grids are implicit graphs: each cell is a node, neighbors are edges
# Same BFS/DFS logic applies — just replace graph[node] with 4-direction checks

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def dfs(r: int, c: int):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if (r, c) in visited or grid[r][c] == '0':
            return
        visited.add((r, c))
        for dr, dc in DIRECTIONS:
            dfs(r + dr, c + dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                islands += 1

    return islands


# BFS version of the same pattern (for shortest path in a grid)
def bfs_grid_shortest_path(grid: List[List[int]], start, end) -> int:
    rows, cols = len(grid), len(grid[0])
    sr, sc = start
    er, ec = end

    if grid[sr][sc] == 1 or grid[er][ec] == 1:   # blocked
        return -1

    visited = {(sr, sc)}
    queue = deque([(sr, sc, 0)])

    while queue:
        r, c, dist = queue.popleft()
        if (r, c) == (er, ec):
            return dist
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and grid[nr][nc] == 0:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

    return -1


# ═══════════════════════════════════════════════════════════════════
# 9. BIPARTITE CHECK
# ═══════════════════════════════════════════════════════════════════
# A graph is bipartite if nodes can be coloured with 2 colours
# such that no two adjacent nodes share a colour
# Equivalent to: contains no odd-length cycle
# Time: O(V + E)  Space: O(V)

def is_bipartite(graph: List[List[int]]) -> bool:
    n = len(graph)
    color = [-1] * n              # -1 = uncoloured

    for start in range(n):
        if color[start] != -1:
            continue
        queue = deque([start])
        color[start] = 0

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]   # alternate colour
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:     # same colour = not bipartite
                    return False

    return True


# ═══════════════════════════════════════════════════════════════════
# COMPLEXITY SUMMARY
# ═══════════════════════════════════════════════════════════════════
#
# Operation              Time        Space     Notes
# ─────────────────────────────────────────────────────────────────
# BFS                    O(V+E)      O(V)      Queue; shortest path unweighted
# DFS                    O(V+E)      O(V)      Stack/recursion
# Cycle (undirected)     O(V+E)      O(V)      Parent tracking in DFS
# Cycle (directed)       O(V+E)      O(V)      3-color (white/gray/black)
# Topo sort (BFS)        O(V+E)      O(V)      In-degree + queue (Kahn's)
# Topo sort (DFS)        O(V+E)      O(V)      Post-order stack, then reverse
# Union-Find find        O(α(n))≈O(1) O(V)    Path compression
# Union-Find union       O(α(n))≈O(1) O(V)    Union by rank
#
# WHICH TO REACH FOR:
#
# Shortest path (unweighted)     → BFS
# Connectivity / path exists     → DFS or Union-Find
# Connected components           → DFS outer loop or Union-Find
# Cycle detection                → DFS (3-color for directed)
# Prerequisite ordering          → Topological sort (Kahn's BFS)
# Dynamic connectivity merging   → Union-Find
# Grid traversal                 → DFS/BFS with 4-direction check
# Bipartite / 2-coloring         → BFS with colour array
#
# NEETCODE PROBLEMS THIS COVERS:
# Number of Islands              → Grid DFS (section 8)
# Clone Graph                    → BFS with hash map
# Course Schedule I/II           → Topo sort / cycle detection (section 5+6)
# Pacific Atlantic Water Flow    → Multi-source BFS from both coastlines
# Number of Connected Components → DFS count (section 4) or Union-Find
# Graph Valid Tree               → Cycle check + connectivity (section 5)
# Word Ladder                    → BFS shortest path (section 2)
# Redundant Connection           → Union-Find (section 7)
# Network Delay Time             → Dijkstra (weighted BFS — next topic)


# ═══════════════════════════════════════════════════════════════════
# QUICK DEMO
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    edges = [[0,1],[0,2],[1,3],[2,3],[3,4]]
    n = 5

    graph = build_undirected(n, edges)
    print("BFS from 0:        ", bfs(graph, 0))
    print("DFS from 0:        ", dfs_iterative(graph, 0))
    print("Shortest 0→4:      ", bfs_shortest_path(graph, 0, 4))
    print("Components:        ", count_components(n, edges))
    print("Has cycle:         ", has_cycle_undirected(n, edges))

    dag_edges = [[0,1],[0,2],[1,3],[2,3],[3,4]]
    print("Topo sort (BFS):   ", topological_sort_bfs(n, dag_edges))
    print("Topo sort (DFS):   ", topological_sort_dfs(n, dag_edges))

    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    print("Components (UF):   ", uf.components)
    print("0 and 4 connected: ", uf.connected(0, 4))

    grid = [["1","1","0"],["0","1","0"],["0","0","1"]]
    print("Islands:           ", num_islands(grid))
