class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = dict()
        
        for ch in s:
            if ch in counts:
                counts[ch] = counts[ch] + 1
            else:
                counts[ch] = 1
        
        for ch in t:
            if ch in counts:
                counts[ch] = counts[ch] - 1
            else:
                return False
        
        return all(count == 0 for count in counts.values())
        