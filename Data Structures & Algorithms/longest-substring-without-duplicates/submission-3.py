class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        res = 0
        while i < len(s):
            j = i
            seen = set()
            
            while j < len(s) and s[j] not in seen:
                seen.add(s[j])
                j += 1
            
            res = max(j - i, res)
            i += 1
            # i = j
            # print(seen)
        
        return res
        