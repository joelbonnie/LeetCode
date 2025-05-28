class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        
        nums.sort()
        pairs = []

        for i, currNum in enumerate(nums):


            if currNum > 0:
                break
            if i > 0 and nums[i-1] == currNum:
                continue

            l = i + 1
            r = len(nums) - 1

            
            while l < r:
                if (nums[l] + nums[r]) == (-currNum):
                    pairs.append([currNum, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while (l < r and nums[l] == nums[l-1]):
                        l+=1
                elif (nums[l] + nums[r]) > (-currNum):
                    r -= 1
                else:
                    l += 1
            

        return pairs

