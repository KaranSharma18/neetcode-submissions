class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
            
        mid = len(nums) // 2
        res = -1
        print
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.search(nums[:mid], target)
        else:
            res = self.search(nums[mid + 1:], target)
            return res if res == -1 else res + mid + 1