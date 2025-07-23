class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatestCandyCount = max(candies)

        willBeGreatest = [True if i + extraCandies >= greatestCandyCount else False for i in candies]
        return willBeGreatest
