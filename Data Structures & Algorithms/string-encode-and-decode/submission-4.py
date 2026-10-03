class Solution:

    def encode(self, strs: List[str]) -> str:
        ss = ""
        
        for s in strs:
            ss += str(len(s)) + s
        
        return ss

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = int(s[i])
            strs.append(s[i + 1: i + j + 1])
            i = i + j + 1
        
        return strs