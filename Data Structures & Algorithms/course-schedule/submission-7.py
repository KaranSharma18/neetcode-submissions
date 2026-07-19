class Solution:
    def build_directed(self, n: int, edges: List[List[int]]) -> dict:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
        
        return graph
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.build_directed(numCourses, prerequisites)
        white, grey, black = 0, 1, 2
        color = [white] * numCourses
        
        def dfs(node):
            color[node] = grey
            for neigbor in graph[node]:
                if color[neigbor] == grey:
                    return True
                if color[neigbor] == white:
                    if dfs(neigbor):
                        return True
                        
            color[node] = black
            return False
            
        for node in range(numCourses):
            if color[node] == white:
                if dfs(node):
                    return False
        return True
        
        
        