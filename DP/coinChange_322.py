class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] * (amount + 1)
        coins.sort()

        minCoins = float('inf')
       

        for i in range(1, amount + 1):
            currentMin = float('inf')
            for coin in coins: 
                remaining = i - coin 
                if remaining < 0:
                    break
                else:
                    currentMin = min(currentMin, 1 + dp[remaining])
            
            dp[i] = currentMin
        
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1 
