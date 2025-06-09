
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Hash Based space O(n) solution
        # numCounter = Counter(nums)
        # return sorted(numCounter.items(), key=lambda x: x[1], reverse = True)[0][0]

        # Boyer-Moore Algorithm 
        curNum, count = None, 0
        for num in nums:
            if count == 0:
                curNum = num
            if num == curNum:
                count += 1
            else:
                count -= 1
        return curNum
