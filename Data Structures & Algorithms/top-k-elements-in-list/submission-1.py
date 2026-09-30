class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        return [i[0] for i in sorted(counts.items(), key = lambda x: x[1], reverse = True)][:k]