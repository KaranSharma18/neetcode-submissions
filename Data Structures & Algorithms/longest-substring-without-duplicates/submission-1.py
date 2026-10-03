class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = s + s[::-1]
        i = 0
        res = 0
        while i < len(ss):
            j = i
            seen = set()
            
            while j < len(ss) and ss[j] not in seen:
                seen.add(ss[j])
                j += 1
            
            res = max(j - i, res)
            i = j
        
        return res
        