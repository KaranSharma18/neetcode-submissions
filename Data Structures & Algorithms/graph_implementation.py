from typing import List
from collections import defaultdict

def build_undirected(n: int, edges: List[List[int]]) -> dict:
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    return graph

def build_directed(n: int, edges: List[List[int]]) -> dict:
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
    
    return graph
    
def dfs(graph: dict, node: int, visited: set, result: List[int]) -> List[int]:
    visited.add(node)
    result.append(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)

def count_components(n: int, edges: List[List[int]]) -> int:
    graph = build_undirected(n, edges)
    visited = set()
    result = []
    count = 0
    
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, result)
            count += 1
    
    return count

def has_cycle_undirected(n: int, edges: List[List[int]]) -> bool:
    graph = build_undirected(n, edges)
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    
    return False
    
def has_cycle_directed(n: int, edges: List[List[int]]) -> bool:
    
    graph = build_directed(n, edges)
    WHITE, GREY, BLACK = 0, 1, 2
    visited = set()
    color = [WHITE] * n
    
    def dfs(node):
        color[node] = GREY
        
        for neighbor in graph[node]:
            if color[neighbor] == WHITE:
                if dfs(neighbor):
                    return True
            if color[neighbor] == GREY:
                return True
            
        
        color[node] = BLACK
        return False
    
    for n in graph:
        if color[n] == WHITE:
            if dfs(n):
                return True
    return False

edges = [[0,2],[1,3],[2,3],[3,4],[7,8]]
n = 5
visited = set()
result = []

graph = build_undirected(n, edges)
dfs(graph, 0, visited, result)
count = count_components(n, edges)
print(has_cycle_undirected(n, edges))
print(graph)
print(result)
print(count)




