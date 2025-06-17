class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Kadane's Algorithm
        maxSum = float('-inf')

        currentSum = float('-inf')
        for num in nums:
            if currentSum < 0:
                currentSum = num
            else:
                currentSum += num
            maxSum = max(maxSum, currentSum)
    
        return maxSum
