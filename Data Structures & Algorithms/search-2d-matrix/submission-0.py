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
        
        for i in range(n):
            if target <= matrix[i][m - 1]:
                return self.search(matrix[i], target)
                
        return False