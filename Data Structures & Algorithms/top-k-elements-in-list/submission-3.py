class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        heap = []
        
        for n, c in count.items():
            heapq.heappush(heap, (c, n))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [n for c, n in heap]