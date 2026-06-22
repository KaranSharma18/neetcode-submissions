class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join([ch.lower() for ch in s if ch.isalnum()])
        i, j = 0, len(clean_s) - 1
        while i < j:
            if clean_s[i] != clean_s[j]:
                return False
            i += 1
            j -= 1

        return True
        