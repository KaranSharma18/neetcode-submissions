class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res_s = ""
        l = []
        for s in strs:
            l.append(str(len(s)))
            
        res_s += ",".join(l)
        res_s += "#"
        for s in strs:
            for ch in s:
                res_s += ch
        
        return res_s

    def decode(self, s: str) -> List[str]:

        if not s:
            return ""
        l, ss = s.split("#", 1)
        
        res = []
        j, k = 0, 0
        for i in l:
            if i == ",":
                continue
            k += int(i)
            res.append(ss[j: k])
            j += k
        
        return res



