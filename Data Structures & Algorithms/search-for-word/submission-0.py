class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        visited = set()
        
        def backtrack(i, j, ind):
            if ind == len(word):
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            if (i, j) in visited:
                return False
            if board[i][j] != word[ind]:
                return False
            
            visited.add((i, j))
            
            found = ((backtrack(i - 1, j, ind + 1)) or
                        backtrack(i + 1, j, ind + 1) or
                        backtrack(i, j - 1, ind + 1) or
                        backtrack(i, j + 1, ind + 1))
            
            visited.remove((i, j))
            return found
            
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
            
        return False
        