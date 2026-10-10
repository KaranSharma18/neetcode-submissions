class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0

        for p in prices:
            if p < buy:
                buy = p
            else:
                res = max(res, p - buy)

        return res