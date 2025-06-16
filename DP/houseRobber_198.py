class Solution:
    def rob(self, nums: List[int]) -> int:

        # # DP Bottom Up 
        # n = len(nums)
        # dp = [0 for _ in range(n)]

        # for i in range(n):
        #     if i == 0:
        #         dp[i] = nums[i]
        #     if i == 1:
        #         dp[i] = max(nums[i], dp[i-1])
        #     if i > 1: 
        #         dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        # return dp[n-1]

        # Space optimized
        two, one = 0, 0 
        for i in range(len(nums)):
            curr = max(nums[i] + two, one)
            two = one 
            one = curr 

        return one  


