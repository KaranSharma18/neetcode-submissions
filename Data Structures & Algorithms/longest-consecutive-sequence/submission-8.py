class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_exist = set(nums)
        cache = {}

        max_length = 0
        for num in nums:
            length = 0
            while num + length in num_exist:
                if num + length in cache:
                    length += cache[num + length]
                    break
                length += 1

            cache[num] = length
            max_length = max(max_length, length)

        return max_length