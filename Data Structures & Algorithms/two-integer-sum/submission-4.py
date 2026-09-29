class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}
        for i, num in enumerate(nums):
            if num not in ind:
                ind[num] = [i]
            else:
                ind[num].append(i)
        print(ind)
        for i, num in enumerate(nums):
            diff = target - num
            if diff in ind:
                for j in ind[diff]:
                    if j != i:
                        return [i, j]
                        
        return None