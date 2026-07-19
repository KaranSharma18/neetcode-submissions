class Solution:
    def build_undirected(self, n: int, edges: List[List[int]]) -> dict:
        graph = defaultdict(list)
        n_componenets = 0
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        return graph
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = self.build_undirected(n, edges)
        visited = set()
        n_componenets = 0
        
        def dfs(node):
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
                    
        for node in range(n):
            if node not in visited:
                n_componenets += 1
                dfs(node)
        return n_componenets
        