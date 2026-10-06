class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda i : i[0]) #sort on start
        prevEndValue = intervals[0][1]
        overlapRemove = 0

        for start, end in intervals[1:]:
            if start < prevEndValue:
                overlapRemove += 1
                if end < prevEndValue:
                    prevEndValue = end
            else:
                prevEndValue = end
        
        return overlapRemove

