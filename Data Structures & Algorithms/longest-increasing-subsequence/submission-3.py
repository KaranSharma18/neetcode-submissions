class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(i):
            # dfs(i) = longest increasing subsequence ENDING at index i
            if i in memo:
                return memo[i]            # Bug 1 fixed: memo[i] not memo[i-1]

            best = 1                      # nums[i] alone is always valid (length 1)
            for j in range(i):            # Bug 4 fixed: try ALL j before i
                if nums[j] < nums[i]:     # Bug 3 fixed: compare chosen prev vs current
                    best = max(best, 1 + dfs(j))

            memo[i] = best                # Bug 1 fixed: store under i
            return memo[i]

        return max(dfs(i) for i in range(n)) 
        