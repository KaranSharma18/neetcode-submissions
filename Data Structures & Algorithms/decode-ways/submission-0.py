class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        hashset = set(map(str, range(1, 27)))
        ways = 0
        memo = {}
        
        def dfs(i):
            if i == n:
                return 1
                
            if i in memo:
                return memo[i]
            
            ways = 0
            
            if s[i] in hashset:
                ways += dfs(i + 1)
            
            if i < n - 1 and s[i: i + 2] in hashset:
                ways += dfs(i + 2)
            
            memo[i] = ways
            return ways
            
        return dfs(0)
        