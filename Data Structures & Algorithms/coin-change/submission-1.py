class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        if not amount:
            return 0
            
        n = len(coins)
        count = 0
        
        for i in range(n - 1, -1, -1):
            while amount >= 0 and coins[i] <= amount:
                amount -= coins[i]
                count += 1
                
        return -1 if amount else count
        