class Solution:

    def encode(self, strs: List[str]) -> str:
        res_s = ""
        for s in strs:
            res_s = res_s + str(len(s)) + "#"
            res_s += s
        
        return res_s

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        i = 0
        j = 0

        while i < len(s):
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            i = j
            if i + l + 1 == len(s):
                res.append(s[i + 1: ])
            else:
                res.append(s[i + 1: i + l + 1])
                
            j = i + l + 1
            i = i + l + 1
        
        return res
