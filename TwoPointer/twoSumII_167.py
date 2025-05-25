class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            calculatedSum = numbers[l] + numbers[r]
            if calculatedSum == target:
                return [l + 1, r + 1]
            elif calculatedSum > target:
                r -= 1
            else:
                l += 1
        
