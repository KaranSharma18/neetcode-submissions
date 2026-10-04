class Solution:
    def is_alnum(self, c: str) -> bool:
        return ("a" <= c <= "z") or ("A" <= c <= "Z") or ("0" <= c <= "9")
        
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
           
            if self.is_alnum(s[i]) and self.is_alnum(s[j]):
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            elif not self.is_alnum(s[i]):
                i += 1
            elif not self.is_alnum(s[j]):
                j -= 1
        
        return True
