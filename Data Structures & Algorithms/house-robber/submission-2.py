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
            tmp = 0
            for j in range(i + 2, n):
                tmp = max(nums[j] + dfs(nums[j], j + 2), tmp)
            memo[nums[i]] = tmp + nums[i]
            print(memo)
            return memo[nums[i]]
            
        res = max(dfs(res, 0), dfs(res, 1))
        return res
        