class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, vals, total):
            if total == target:
                res.append(vals[:])
                return
            
            for i in range(start, len(nums)):
                if total > target:
                    return
                vals.append(nums[i])
                backtrack(i, vals, total + nums[i])
                vals.pop()
        
        backtrack(0, [], 0)
        return res

            