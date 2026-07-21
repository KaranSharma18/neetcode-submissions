class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        res = 0
        
        def dfs(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            tmp = 0
            for j in range(i + 2, n):
                tmp = max(nums[j] + dfs(j + 2), tmp)
            memo[i] = tmp + nums[i]
            return memo[i]
            
        res = max(dfs(0), dfs(1))
        print(memo)
        return res
        