class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            counts = {}
            
            for ch in s:
                counts[ch] = counts.get(ch, 0) + 1
            groups.setdefault(frozenset(counts), []).append(s)
        
        return list(groups.values())