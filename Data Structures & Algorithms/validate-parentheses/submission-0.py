class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "}": "{", "]": "["}
        
        st = []
        for ch in s:
            if ch not in pairs:
                st.append(ch)
            else:
                if not st or pairs[ch] != st[-1]:
                    return False
                st.pop()
                
        return not st
        