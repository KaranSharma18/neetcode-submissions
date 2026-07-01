class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[r]:       # left half is sorted
                if nums[r] < target < nums[mid]:
                    r = mid - 1           # target in left sorted half
                else:
                    l = mid + 1           # target in right half
            else:                          # right half is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1           # target in right sorted half
                else:
                    r = mid - 1           # target in left half

        return -1