class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = defaultdict(list)
        
        for i, num in enumerate(nums):
            index_map[num].append(i)
            
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in index_map:
                ind_lst = index_map[diff]
                if len(ind_lst) > 1:
                    return sorted(ind_lst)
                elif ind_lst[0] != i:
                    return sorted([i, ind_lst[0]])
        