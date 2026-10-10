def merge_sort(nums: List[int]) -> List[int]:
    
    n = len(nums)
    if n < 2:
        return nums
    
    mid = n // 2
    
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    
    res = []
    
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
            
    res.extend(left[i:])
    res.extend(right[j:])
    
    return res

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums = merge_sort(nums)
        
        for k in range(n - 2):
            i, j = k + 1, n - 1
            
            while i < j:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    i += 1
                    j -= 1
                    
                elif total < 0:
                  i += 1
                else:
                     j -= 1
                     
        return [list(t) for t in res] if res else []