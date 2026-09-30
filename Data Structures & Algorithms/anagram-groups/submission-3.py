class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = {}
        
        for s in strs:
            s_sorted = "".join(sorted(s))
            # print(s_sorted)
            group_anagrams[s_sorted] = group_anagrams.setdefault(s_sorted, []) + [s]
        
        return list(group_anagrams.values())