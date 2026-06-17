class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
            
        for s in strs:
            s_srt = "".join(sorted(s))
            appended = False
            for lst in res:
                for r in lst:
                    rr = "".join(sorted(r))
                    if rr == s_srt:
                        lst.append(s)
                        appended = True
                        break
                if appended:
                    break
            if not appended:
                res.append([s])
        return res
        