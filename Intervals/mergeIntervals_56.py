class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        mergedIntervals = [intervals[0]]

        currentInterval = 0 
        for i in range(1, len(intervals)):
            if intervals[i][0] <= mergedIntervals[currentInterval][1]:
                mergedIntervals[currentInterval] = [mergedIntervals[currentInterval][0], 
                max(mergedIntervals[currentInterval][1], intervals[i][1])]
            else:
                mergedIntervals.append(intervals[i])
                currentInterval += 1
        
        return mergedIntervals
            
