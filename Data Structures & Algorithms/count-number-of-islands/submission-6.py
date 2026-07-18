class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], (-1, 0), [0, 1], [0, -1]]
        count = 0
        
        def dfs(i, j):
            if i >= rows or i < 0 or j >= cols or j < 0:
                return 
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            for dr, dc in directions:
                dfs(i + dr, j + dc)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        
        return count
        