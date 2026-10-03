class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        res = 0
        
        def dfs(res, i):
            if i >= n:
                return 0
            if nums[i] in memo:
                return memo[nums[i]]
            tmp1, tmp2 = 0, 0
            for j in range(i + 2, n):
                tmp1 = nums[j] + dfs(nums[j], j + 2)
                memo[nums[j]] = tmp1
                tmp2 = max(tmp2, tmp1)
            memo[nums[i]] = tmp2 + nums[i]
            print(memo)
            return memo[nums[i]]
            
        res = max(dfs(res, 0), dfs(res, 1))
        return res
        