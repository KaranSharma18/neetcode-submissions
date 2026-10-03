class Solution:
    def build_undirected(self, n: int, edges: List[List[int]]) -> dict:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        return graph

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = self.build_undirected(n, edges)
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
            
        for node in range(n):
            if node not in visited:
                if dfs(node, -1):
                    return False
        return True
        