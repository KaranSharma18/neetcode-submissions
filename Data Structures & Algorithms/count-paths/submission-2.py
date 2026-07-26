class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[1] * n for _ in range(m)]   # top row and left col are all 1
        dp = [1] * n
        for r in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c - 1]  # from above + from left
        
        print(dp)
        return dp[n - 1]