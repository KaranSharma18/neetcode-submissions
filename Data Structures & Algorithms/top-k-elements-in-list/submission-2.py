class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        top = sorted(counts.items(), key = lambda x: x[1], reverse = True)
        
        return [n for n, _ in top[:k]]