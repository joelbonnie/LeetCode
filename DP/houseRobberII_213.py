class Solution:

    def rob(self, nums: List[int]) -> int:
        def maxLick(currNums):
            twoBack, oneBack = 0,0 
            for i in range(len(currNums)):
                curr = max(twoBack + currNums[i], oneBack)
                twoBack = oneBack
                oneBack = curr 
            return oneBack

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        return max(maxLick(nums[1:]), maxLick(nums[:len(nums) - 1]))

