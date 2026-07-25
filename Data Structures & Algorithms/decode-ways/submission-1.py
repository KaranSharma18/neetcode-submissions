class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        hashset = set(map(str, range(1, 27)))
        dp[0] = 1
        dp[1] = 1 if s[0] in hashset else 0
        
        for i in range(2, n + 1):
            if s[i - 1] in hashset:
                dp[i] += dp[i - 1]
            if s[i - 2: i] in hashset:
                dp[i] += dp[i - 2]
                
        return dp[n]
        