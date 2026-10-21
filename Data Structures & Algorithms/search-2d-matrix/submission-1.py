class Solution:
    def search(self, nums: List[int], target: int):
        l, h = 0, len(nums)
        while l < h:
            mid = (l + h) // 2
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                h = mid
            else:
                l = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, h = 0, n
        
        while l < h:
            mid = (l + h) // 2
            if target <= matrix[mid][m - 1]:
                h = mid
            else:
                l = mid + 1
        
        if l == n:
            return False
        return self.search(matrix[l], target)
    