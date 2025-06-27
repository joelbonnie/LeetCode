class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # Diabolical runtime - fix 
        n = len(nums)
        dp = [float('inf')] * len(nums)
        dp[n-1] = 0 
        for i in range(n-2, -1, -1):
            if nums[i] >= (n - 1 - i): 
                dp[i] = 1
            else: 
                for j in range(nums[i]):
                    dp[i] = min(dp[i], 1 + dp[i + j + 1])
        return dp[0]
