class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cp, sp = 100000000000, 0
        
        for i, price in enumerate(prices):
            
            if price < cp:
                cp = price
            else:
                sp = max(sp, price)
                profit = max(profit, sp - cp)
        
        return profit
        