class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        finalIntervals = []

        for i in range(len(intervals)): 
            if newInterval[1] < intervals[i][0]:
                finalIntervals.append(newInterval)
                return finalIntervals + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                finalIntervals.append(intervals[i])
            else: 
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        
        finalIntervals.append(newInterval)
        return finalIntervals



                

