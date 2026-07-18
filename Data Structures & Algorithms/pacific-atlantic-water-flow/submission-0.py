class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights),len(heights[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = []

        def dfs(i, j, prev, visited):
            nonlocal pacific, atlantic
            if i < 0 or j < 0:
                pacific = True
                return 
            if i >= rows or j >= cols:
                atlantic = True
                return
            if heights[i][j] > prev:
                return
            if (i, j) in visited:
                return

            visited.add((i, j))
            for dr, dc in directions:
                dfs(i + dr, j + dc, heights[i][j], visited)
                if pacific and atlantic:
                    break
        
        
        for i in range(rows):
            for j in range(cols):
                pacific = atlantic = False
                dfs(i, j, float("inf"), set())
                if pacific and atlantic:
                    res.append([i, j])
        
        return res
        