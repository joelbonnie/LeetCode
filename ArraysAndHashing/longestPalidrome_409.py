from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        stringCounter = Counter(s)
        middleFlag = False
        totalLen = 0 
        for count in stringCounter.values():
            if not middleFlag and count % 2 == 1:
                totalLen += (count // 2) * 2 + 1 
                middleFlag = True
            else:
                totalLen += (count // 2) * 2
        return totalLen
