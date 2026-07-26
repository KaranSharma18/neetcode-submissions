class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = set(wordDict)        # Issue 1 fixed
        n = len(s)
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j >= n:              # Issue 2 fixed
                return s[i:j+1] in seen

            # Issue 3, 4 fixed: short-circuit prevents redundant dfs(i, j+1)
            # when s[i:j+1] is a valid word AND the suffix also segments
            result = (s[i:j+1] in seen and dfs(j+1, j+1)) or dfs(i, j+1)
            memo[(i, j)] = result
            return result

        return dfs(0, 0)