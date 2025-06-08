class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, u = 0, len(nums) - 1
        rightMostElement = nums[-1]


        while l <= u: 
            m = (l+u) // 2
            if nums[m] == target:
                return m 
            
            if target > rightMostElement:
                if nums[m] > rightMostElement:
                    if nums[m] > target:
                        u = m - 1
                    else:
                        l = m + 1
                else: 
                    u = m - 1
            else:
                if nums[m] <= rightMostElement:
                    if nums[m] > target:
                        u = m - 1
                    else:
                        l = m + 1
                else:
                    l = m + 1
        return -1
                    


