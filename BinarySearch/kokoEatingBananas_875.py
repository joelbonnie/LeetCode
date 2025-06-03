class Solution:
    def minEatingSpeed (self, piles: List[intl, h: int) -> int:
        l, u = 1, max(piles)
        while l < u:
            k = (l + u) // 2
            t = sum([(pile + k - 1) // k for pile in piles])
            if t <= h:
                u = k
            else:
                l = k+1
        return l