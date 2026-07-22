class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        res_len = 0
        
        def helper(l, r):
            nonlocal res_len, res
            while l >= 0 and r < n and s[l] == s[r]:
                if res_len < (r - l + 1):
                    res = s[l: r + 1]
                    res_len = r - l + 1
                l -= 1
                r += 1
                
        for i in range(n):
            helper(i, i)    # odd lenght palindrome
            helper(i, i + 1)    # even lenght palindrome
        
        return res
        