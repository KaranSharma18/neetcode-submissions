class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j, l = 0, 0, 0
        res = 0
        count = dict()
        
        while j < len(s):
            count[s[j]] = count.get(s[j], 0) + 1
            m_ch = max(count.values())
            l = j - i + 1
            if (l - m_ch) <= k:
                res = max(res, l)
            else:
                count[s[i]] -= 1
                i += 1
            
            j += 1
        
        return res

        