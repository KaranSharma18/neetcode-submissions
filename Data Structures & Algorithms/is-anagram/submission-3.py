class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        ch = [0] * 26
        
        for ch_s, ch_t in zip(s, t):
            ch[ord(ch_s) - ord("a")] += 1
            ch[ord(ch_t) - ord("a")] -= 1
        
        for count in ch:
            if count != 0:
                return False
        return True
        