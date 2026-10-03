class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        end = ((target - 1) // 2) + 1
        
        index_map = defaultdict(list)
        
        for i, num in enumerate(nums):
            index_map[num].append(i)
            
        for i in range(target, end - 1, -1):
            diff = target - i
            
            if i in index_map and diff in index_map:
                indlist_i, indlist_diff = index_map[i], index_map[diff]
                
                if len(indlist_i) > 1:
                    return sorted(indlist_i)
                else:
                    return (sorted(indlist_i + indlist_diff))
        