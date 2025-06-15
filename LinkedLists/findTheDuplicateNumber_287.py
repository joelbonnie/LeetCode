class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        first = nums[0]
        second = slow 

        while first != second:
            first = nums[first]
            second = nums[second]
        
        return first 
