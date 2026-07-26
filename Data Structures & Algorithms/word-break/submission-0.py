class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = set()
        n = len(s)
        memo = {}
        
        for word in wordDict:
            seen.add(word)
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
                
            if j >= n and s[i: j + 1] not in seen:
                return False
            if j >= n and s[i: j + 1] in seen:
                return True
            
            a, b = False, False
            if s[i: j + 1] in seen:
                a = dfs(j + 1, j + 1)
                
            b = dfs(i, j + 1)
            
            memo[(i, j)] = a or b
                
            return a or b
                
        if dfs(0, 0):
            return True
        return False
        