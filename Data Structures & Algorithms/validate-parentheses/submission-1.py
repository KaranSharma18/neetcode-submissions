class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b = {"]": "[", "}": "{", ")": "("}
        
        for ch in s:
            if ch in b:
                if stack and stack[-1] == b[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return False if stack else True