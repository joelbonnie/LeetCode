# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, u = 1, n
        while l < u: 
            m = l + (u - l) // 2 
            if isBadVersion(m):
                u = m 
            else: 
                l = m + 1 
        return l 

