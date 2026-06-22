class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean_s = "".join([ch.lower() for ch in s if ch.isalnum()])
        clean_s = s
        i, j = 0, len(clean_s) - 1
        while i < j:
            while i < j and not clean_s[i].isalnum():
                i += 1
            while i < j and not clean_s[j].isalnum():
                j -= 1
            if clean_s[i].lower() != clean_s[j].lower():
                return False
            i += 1
            j -= 1

        return True
        