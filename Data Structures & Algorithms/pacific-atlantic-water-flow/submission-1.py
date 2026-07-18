class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        visited = set()
        at,  pc = set(), set()
        res = []
        
        def dfs(i, j, prev, visited):
            if i < 0 or j < 0 or i == rows or j == cols or (i, j) in visited or heights[i][j] < prev:
                return
            
            visited.add((i, j))
            dfs(i - 1, j, heights[i][j], visited)
            dfs(i + 1, j, heights[i][j], visited)
            dfs(i, j - 1, heights[i][j], visited)
            dfs(i, j + 1, heights[i][j], visited)
        
        for r in range(rows):
            dfs(r, 0, heights[r][0], pc)
            dfs(r, cols - 1, heights[r][cols - 1], at)
            
        for c in range(cols):
            dfs(0, c, heights[0][c], pc)
            dfs(rows - 1, c, heights[rows - 1][c], at)
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) in at and (i, j) in pc:
                    res.append([i, j])
        return res
        