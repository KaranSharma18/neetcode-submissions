class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        i, j = 0, 0
        res = 0
        
        while j < len(s):
            ch = s[j]
            if ch in seen and seen[ch] >= i:
                i = seen[ch] + 1

            seen[ch] = j
            res = max(j - i + 1, res) 
            j += 1
        
        return res

