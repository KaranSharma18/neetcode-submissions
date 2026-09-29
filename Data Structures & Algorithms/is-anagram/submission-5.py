class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count = {}
        for ch1, ch2 in zip(s, t):
            count[ch1] = count.get(ch1, 0) + 1
            count[ch2] = count.get(ch2, 0) - 1
        
        return all(i == 0 for i in count.values())