class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)

        while stones and len(stones) > 1:

            firstRock = -heapq.heappop(stones)
            secondRock = -heapq.heappop(stones)
            if firstRock == secondRock:
                continue 
            # firstRock is heavier 
            weightDiff = firstRock - secondRock
            heapq.heappush(stones, -weightDiff)

        if stones:
            return -stones[0]
        return 0
