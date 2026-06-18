class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        
        for s in strs:
            sorted_s = "".join(sorted(s))
            
            for group in res:
                if "".join(sorted(group[0])) == sorted_s:
                    group.append(s)
                    break
            else:
                res.append([s])
        
        return res
                