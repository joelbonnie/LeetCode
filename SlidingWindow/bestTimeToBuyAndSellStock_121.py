class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0

        maxProfit = 0 
        minBuy = prices[0]
        
        for currentPrice in prices:
            currentProfit = currentPrice - minBuy

            if currentProfit > maxProfit:
                maxProfit = currentProfit 
            
            if currentPrice < minBuy:
                minBuy = currentPrice 
        
        return maxProfit


