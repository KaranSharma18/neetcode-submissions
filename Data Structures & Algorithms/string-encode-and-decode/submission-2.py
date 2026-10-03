class Solution:

    def encode(self, strs: List[str]) -> str:

        res_s = ""
        for s in strs:
            res_s += str(len(s))
            res_s += s
        
        return res_s


    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        i = 0

        while i < len(s):
            l = int(s[i])
            if i + l + 1 == len(s):
                res.append(s[i + 1: ])
            else:
                res.append(s[i + 1: i + l + 1])
            i = i + l + 1 
        
        return res



