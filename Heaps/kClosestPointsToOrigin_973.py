class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    
        pointDistMap = {}
        for currentPoint in points: 
            # Not using square roots since for all x,y >= 0, x > y => sqrt(x) > sqrt(y) 
            distSquared = currentPoint[0]**2 + currentPoint[1]**2
            if pointDistMap.get(distSquared):
                pointDistMap[distSquared].append(currentPoint)
            else:
                pointDistMap[distSquared] = [currentPoint]

        
        distHeap = list(pointDistMap.keys())
        heapq.heapify(distHeap)

        kClosestPoints = []
        while k: 
            currentDist = heapq.heappop(distHeap)
            for currentPoint in pointDistMap[currentDist]:
                # We can add all the points since the answer is said to be unique 
                kClosestPoints.append(currentPoint)
                k-=1

        return kClosestPoints
