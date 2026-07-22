class Solution:
    def is_palindrome(self, ss) -> bool:
        return ss == ss[::-1]

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        for i in range(n):
            for j in range(i + 1, n + 1):
                ss = s[i: j]
                # print(f"ss: {ss}")
                if self.is_palindrome(ss) and len(ss) > len(res):
                    res = ss
        return res if res else s
        