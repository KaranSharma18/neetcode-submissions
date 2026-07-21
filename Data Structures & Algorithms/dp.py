from typing import List
from functools import lru_cache


# ================================================================
# DYNAMIC PROGRAMMING — COMPLETE REFERENCE
# ================================================================
#
# WHAT IS DP?
# Solving problems by breaking them into OVERLAPPING SUBPROBLEMS
# and STORING results to avoid recomputing them.
#
# TWO REQUIRED PROPERTIES:
# 1. Overlapping Subproblems  — same subproblems appear repeatedly
# 2. Optimal Substructure     — optimal solution built from optimal sub-solutions
#
# SIGNALS THAT A PROBLEM IS DP:
#   "minimum/maximum number of X"
#   "count all ways to do X"
#   "can we achieve X"
#   "longest/shortest subsequence/path"
#   Choices at each step that affect future choices
#   Brute force would be exponential
#
# ─────────────────────────────────────────────────────────────────
# THE 5-STEP FRAMEWORK (apply to every DP problem)
# ─────────────────────────────────────────────────────────────────
#
# Step 1 RECOGNIZE  — does it have the two DP properties?
# Step 2 DEFINE     — what does dp[i] or dp[i][j] MEAN exactly?
#                     "dp[i] = max profit considering first i items"
#                     This is the hardest step. Be precise.
# Step 3 RECURRENCE — how does dp[i] relate to smaller subproblems?
#                     "dp[i] = max(dp[i-1], dp[i-2] + nums[i])"
# Step 4 BASE CASES — what are the smallest problems you know directly?
#                     "dp[0] = 0, dp[1] = nums[0]"
# Step 5 ORDER      — in what order to fill the table?
#                     Usually left→right for 1D, top-left→bottom-right for 2D
#
# TWO APPROACHES:
# Top-down  (Memoization) — recursion + cache — mirrors problem definition naturally
# Bottom-up (Tabulation)  — iterative, fills table — usually faster in practice
#
# ================================================================
# SECTION 1: FIBONACCI — THE CANONICAL DP EXAMPLE
# ================================================================

# ── NAIVE: O(2^n) time — recomputes the same values exponentially ──
def fib_naive(n: int) -> int:
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)
# fib(40) makes 2^40 ≈ 1 billion calls. Unusable.


# ── TOP-DOWN (memoization): O(n) time, O(n) space ──
def fib_memo(n: int, memo: dict = {}) -> int:
    if n in memo:
        return memo[n]         # cache hit — return stored result instantly
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
# Or use Python's built-in decorator: @lru_cache(maxsize=None)


# ── BOTTOM-UP (tabulation): O(n) time, O(n) space ──
def fib_dp(n: int) -> int:
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1                  # base cases
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]    # recurrence
    return dp[n]


# ── SPACE OPTIMIZED: O(n) time, O(1) space ──
# Notice: dp[i] only needs dp[i-1] and dp[i-2] — don't need full array
def fib_optimized(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ================================================================
# SECTION 2: CLIMBING STAIRS
# ================================================================
# State:      dp[i] = number of ways to reach step i
# Recurrence: dp[i] = dp[i-1] + dp[i-2]
#             (arrive from step i-1 by taking 1 step, or from i-2 by taking 2)
# Base cases: dp[1] = 1, dp[2] = 2
# This is Fibonacci in disguise.

def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


# ================================================================
# SECTION 3: HOUSE ROBBER
# ================================================================
# State:      dp[i] = max money robbing from houses 0..i
# Recurrence: dp[i] = max(dp[i-1],         # skip house i
#                         dp[i-2] + nums[i]) # rob house i + best 2 ago
# Base cases: dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
# Key insight: can't rob adjacent houses, so choice at each house is
#              "rob this one (can't use i-1)" or "skip (keep best so far)"

def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    a, b = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        a, b = b, max(b, a + nums[i])
    return b


# ================================================================
# SECTION 4: JUMP GAME
# ================================================================
# State:      dp[i] = True if index i is reachable
# Recurrence: dp[i] = any(dp[j] and j + nums[j] >= i for j < i)
# But greedy is O(n): track max reachable index

def canJump(nums: List[int]) -> bool:
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:       # can't reach this index
            return False
        max_reach = max(max_reach, i + jump)
    return True


# ================================================================
# SECTION 5: COIN CHANGE (unbounded — each coin usable many times)
# ================================================================
# State:      dp[i] = min coins needed to make amount i
# Recurrence: dp[i] = min(dp[i - coin] + 1) for each coin ≤ i
# Base case:  dp[0] = 0 (0 coins needed to make amount 0)
# Init:       dp[i] = inf for all i > 0 (unknown initially)
# Order:      left → right (dp[i] needs smaller amounts)

def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


# ================================================================
# SECTION 6: LONGEST INCREASING SUBSEQUENCE (LIS)
# ================================================================
# State:      dp[i] = length of LIS ending at index i
# Recurrence: dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]
# Base case:  dp[i] = 1 (every element alone is an LIS of length 1)
# Answer:     max(dp)
# Time: O(n²) — O(n log n) possible with binary search (patience sorting)

def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# ================================================================
# SECTION 7: UNIQUE PATHS (2D grid DP)
# ================================================================
# State:      dp[i][j] = number of paths to reach cell (i,j)
# Recurrence: dp[i][j] = dp[i-1][j] + dp[i][j-1]  (from top or left)
# Base cases: dp[0][j] = 1 (top row: only one way — all right)
#             dp[i][0] = 1 (left col: only one way — all down)
# Key insight: you can only move right or down

def uniquePaths(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]  # first row and col already 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]


# ================================================================
# SECTION 8: LONGEST COMMON SUBSEQUENCE (LCS)
# ================================================================
# State:      dp[i][j] = LCS of text1[:i] and text2[:j]
# Recurrence: if text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
#             else:                          dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# Base cases: dp[0][j] = 0, dp[i][0] = 0 (LCS with empty string = 0)
# Key insight: when chars match, extend the previous LCS by 1
#              when they don't, take the best of skipping either char

def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1    # chars match — extend
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # take best of skipping

    return dp[m][n]


# ================================================================
# SECTION 9: EDIT DISTANCE (Levenshtein Distance)
# ================================================================
# State:      dp[i][j] = min edits to convert word1[:i] to word2[:j]
# Recurrence: if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
#             else: dp[i][j] = 1 + min(
#                 dp[i-1][j],     # delete from word1
#                 dp[i][j-1],     # insert into word1
#                 dp[i-1][j-1]    # replace
#             )
# Base cases: dp[i][0] = i (delete all i chars)
#             dp[0][j] = j (insert all j chars)

def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i    # cost of deleting all chars
    for j in range(n + 1):
        dp[0][j] = j    # cost of inserting all chars

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]   # no edit needed
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],     # delete
                    dp[i][j-1],     # insert
                    dp[i-1][j-1]    # replace
                )

    return dp[m][n]


# ================================================================
# SECTION 10: WORD BREAK
# ================================================================
# State:      dp[i] = True if s[:i] can be segmented using wordDict
# Recurrence: dp[i] = True if any dp[j] is True AND s[j:i] is in word_set
# Base case:  dp[0] = True (empty string is always valid)
# Order:      left → right

def wordBreak(s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break   # found one valid split — no need to check others

    return dp[n]


# ================================================================
# SECTION 11: 0/1 KNAPSACK (each item used at most once)
# ================================================================
# State:      dp[i][w] = max value using first i items with capacity w
# Recurrence: dp[i][w] = max(
#                 dp[i-1][w],                          # skip item i
#                 dp[i-1][w - weights[i-1]] + values[i-1]  # take item i (if fits)
#             )
# Base case:  dp[0][w] = 0 (no items → no value)
# Key insight: for each item, decide to include or exclude

def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]                        # skip item i
            if weights[i-1] <= w:                          # item fits
                dp[i][w] = max(dp[i][w],
                               dp[i-1][w - weights[i-1]] + values[i-1])

    return dp[n][capacity]


# ================================================================
# SPACE OPTIMIZATION: 2D → 1D
# ================================================================
# Many 2D DP problems only look at the PREVIOUS ROW — so you
# can reduce O(m*n) space to O(n) by keeping just one row.

def knapsack_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        # traverse RIGHT TO LEFT to avoid using item i twice
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]
# Why right to left? If we went left→right, dp[w - weight] would already
# include item i (updated in this same pass). Right→left ensures we
# still see the "before item i" values, i.e. dp[i-1] row semantics.


# ================================================================
# COMMON MISTAKES
# ================================================================
#
# 1. WRONG STATE DEFINITION
#    Bad:  "dp[i] = something about index i" (vague)
#    Good: "dp[i] = max profit if we MUST rob house i"  (precise)
#          or "dp[i] = max profit considering houses 0..i" (also precise)
#    The recurrence flows from the definition. Wrong definition = wrong recurrence.
#
# 2. FORGETTING BASE CASES
#    If dp[i] depends on dp[i-1] and dp[i-2], you need BOTH base cases.
#    If dp[0][j] or dp[i][0] aren't explicitly set, you get wrong results.
#
# 3. WRONG TRAVERSAL ORDER
#    If dp[i] depends on dp[i-1], you must fill left → right.
#    If dp[i] depends on dp[i+1], fill right → left.
#    2D: usually top-left → bottom-right.
#    Knapsack space-optimized: must go right → left within each row.
#
# 4. OFF-BY-ONE ERRORS IN 2D DP
#    dp[i][j] usually represents s1[:i] and s2[:j] (0 = empty string).
#    So dp[m][n] is the answer, not dp[m-1][n-1].
#    The indices in the recurrence shift by 1: dp[i][j] uses s1[i-1], s2[j-1].
#
# 5. INITIALIZING WITH WRONG DEFAULT
#    If you want minimum: initialize to float('inf'), NOT 0.
#    If you want maximum: initialize to float('-inf') or 0 if values ≥ 0.
#    dp[0] is often the only 0 (the base case).


# ================================================================
# COMPLEXITY REFERENCE
# ================================================================
#
# Problem                   Time         Space       Key Pattern
# ─────────────────────────────────────────────────────────────────
# Fibonacci                 O(n)         O(1)*       1D linear
# Climbing Stairs           O(n)         O(1)*       1D linear (= fib)
# House Robber              O(n)         O(1)*       1D linear with skip
# Jump Game                 O(n)         O(1)        Greedy (DP not needed)
# Coin Change               O(n * m)     O(n)        1D, m = num coins
# LIS                       O(n²)        O(n)        1D with inner scan
# Word Break                O(n²)        O(n)        1D with inner scan
# Unique Paths              O(m * n)     O(n)*       2D grid, 1 row
# LCS                       O(m * n)     O(m * n)    2D string
# Edit Distance             O(m * n)     O(m * n)    2D string
# 0/1 Knapsack              O(n * W)     O(W)*       2D → 1D optimized
#
# * after space optimization (keep only previous row/two values)
#
# RECOGNIZING THE PATTERN:
# "min/max"                 → try DP (build optimal from sub-optimal)
# "count ways"              → try DP (sum subproblem counts)
# "can we achieve"          → try DP (boolean — OR of subproblems)
# "longest/shortest subseq" → LCS, LIS, or similar 2D pattern
# "string transformation"   → edit distance pattern
# "grid traversal, count"   → unique paths pattern
# "items with constraint"   → knapsack pattern


# ================================================================
# QUICK DEMO
# ================================================================

if __name__ == "__main__":
    print("=== 1D DP ===")
    print("Fibonacci(10):        ", fib_optimized(10))              # 55
    print("Climbing stairs(5):   ", climbStairs(5))                 # 8
    print("House robber:         ", rob([2,7,9,3,1]))               # 12

    print("\n=== Decision DP ===")
    print("Coin change(11):      ", coinChange([1,5,6,9], 11))      # 2
    print("Word break:           ", wordBreak("leetcode", ["leet","code"]))  # True
    print("Jump game:            ", canJump([2,3,1,1,4]))           # True

    print("\n=== Subsequence DP ===")
    print("LIS:                  ", lengthOfLIS([10,9,2,5,3,7,101,18]))  # 4

    print("\n=== 2D DP ===")
    print("Unique paths(3x7):    ", uniquePaths(3, 7))              # 28
    print("LCS:                  ", longestCommonSubsequence("abcde","ace"))  # 3
    print("Edit distance:        ", minDistance("horse","ros"))     # 3

    print("\n=== Knapsack ===")
    print("0/1 Knapsack:         ", knapsack([1,3,4,5],[1,4,5,7],7))  # 9
    print("Knapsack optimized:   ", knapsack_optimized([1,3,4,5],[1,4,5,7],7))  # 9
