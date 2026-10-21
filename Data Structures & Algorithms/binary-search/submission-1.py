class Solution:
    def binary_search(self, nums: List[int], l: int, h: int, target: int) -> int:
        if l >= h:
            return -1
        
        mid = (l + h) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(nums, l, mid, target)
        else:
            return self.binary_search(nums, mid + 1, h, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums), target)