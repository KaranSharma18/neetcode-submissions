class Solution:
    def climbStairs(self, n: int, memo: dict = {}) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        
        if n in memo:
            return memo[n]
        
        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
        return memo[n]