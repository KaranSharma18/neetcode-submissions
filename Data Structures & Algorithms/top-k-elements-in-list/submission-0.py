class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        
        for num in nums:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1
        
        arr = [[] for _ in range(len(nums) + 1)]
        for num, c in count.items():
            arr[c].extend([num])
        
        res = []
        i = len(arr) - 1
        
        flattened = [num for group in reversed(arr) for num in group]
        
        return flattened[:k]

        