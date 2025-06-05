class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxSequenceLength = 0

        for currentNumber in numset:
            if (currentNumber - 1) not in numset:
                currentSequenceLength = 1
                while (currentNumber + currentSequenceLength) in numset:
                    currentSequenceLength += 1
                
                maxSequenceLength = max(currentSequenceLength, maxSequenceLength)
        return maxSequenceLength
        


