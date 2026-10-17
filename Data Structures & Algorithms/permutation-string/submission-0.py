class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
            
        counts1, counts2 = {}, {}
        for ch1 in s1:
            counts1[ch1] = counts1.get(ch1, 0) + 1
        
        for i in range(n1):
            ch = s2[i]
            if ch in counts1:
                counts2[ch] = counts2.get(ch, 0) + 1
        
        
        
        i, j = 0, n1 - 1
        while j < n2:
            if counts2 == counts1:
                return True
            
            if s2[i] in counts2:
                counts2[s2[i]] -= 1
                
            i += 1
            j += 1
            
            
            if j < n2 and s2[j] in counts1:
                counts2[s2[j]] = counts2.get(s2[j], 0) + 1
                
        return False