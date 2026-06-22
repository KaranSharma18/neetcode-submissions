class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join([ch.lower() for ch in s if ch.isalnum()])
        i, j = 0, len(clean_s) - 1
        while i < j:
            if clean_s[i] == " " or not clean_s[i].isalnum():
                i += 1
                continue
            if clean_s[j] == " " or not clean_s[j].isalnum():
                j -= 1
                continue
            if clean_s[i].lower() != clean_s[j].lower():
                return False
            i += 1
            j -= 1

        return True
        