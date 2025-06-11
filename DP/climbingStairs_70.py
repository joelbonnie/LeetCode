class Solution:
    seenStairs = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:

        # Memoization - Top Down 
        # if self.seenStairs.get(n):
        #     return self.seenStairs[n]
        # else: 
        #     if self.seenStairs.get(n-1):
        #         firstWay = self.seenStairs[n-1]
        #     else:
        #         firstWay = self.climbStairs(n-1)
        #         self.seenStairs[n-1] = firstWay

        #     if self.seenStairs.get(n-2):
        #         secondWay = self.seenStairs[n-2]
        #     else:
        #         secondWay = self.climbStairs(n-2)
        #         self.seenStairs[n-2] = secondWay

        #     return firstWay + secondWay

        # DP - Bottom Up
        # seenStairs = {1: 1, 2: 2}

        # for i in range(3,n+1):
        #     seenStairs[i] = seenStairs[i-1] + seenStairs[i-2]
        
        # return seenStairs[n]
            

        # DP 
        first, second = 1, 1
        for i in range(2, n+1):
            temp = second
            second = first + second 
            first = temp
        
        return second
