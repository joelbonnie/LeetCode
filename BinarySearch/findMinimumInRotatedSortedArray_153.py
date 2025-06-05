class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, u = 0, len(nums) - 1
        rightMostNumber = nums[-1]

        while l < u: 
            m = (l + u) // 2
            if nums[m] > rightMostNumber:
                l = m + 1
            else: 
                u = m 
        return nums[l]
