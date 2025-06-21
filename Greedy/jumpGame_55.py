class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # Greedy 

        # if len(nums) == 1: return True 

        # currentMaxJumpPos = 0 
        # target = len(nums) - 1

        # for i in range(len(nums) - 1):
        #     if currentMaxJumpPos < i: 
        #         break 
        #     currentMaxJumpPos = max(currentMaxJumpPos, i + nums[i])
        #     if currentMaxJumpPos >= target:
        #         return True 

        # return False


        # Cleaner
        target = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1): 
            if nums[i] + i >= target: 
                target = i 
        
        return target == 0 

