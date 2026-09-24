class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_c, t_c = {}, {}
        
        for ch_s, ch_t in zip(s, t):
            s_c[ch_s] = s_c.get(ch_s, 0) + 1
            t_c[ch_t] = t_c.get(ch_t, 0) + 1
        
        return s_c == t_c
        