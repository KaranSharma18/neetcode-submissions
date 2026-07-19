class Solution:
    def build_directed(self, n: int, edges: List[List[int]]) -> dict:
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        return in_degree, graph
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree, graph = self.build_directed(numCourses, prerequisites)
        queue = deque([])
        order = []
        
        for node in range(numCourses):
            if in_degree[node] == 0:
                queue.append(node)
                
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) == numCourses:
            return True

        return False
        
        
        