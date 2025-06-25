class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mul = 1
        r_mul = 1
        n = len(nums)

        prefix = [0] * n
        suffix = [0] * n 

        for i in range(n):
            prefix[i] = l_mul 
            l_mul *= nums[i]

        for i in range(n-1, -1, -1): 
            suffix[i] = r_mul
            r_mul *= nums[i]
        
        resultArr = []
        for i in range(n):
            resultArr.append(prefix[i] * suffix[i])
        
        return resultArr

