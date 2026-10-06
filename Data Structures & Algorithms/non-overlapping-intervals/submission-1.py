class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        lastKnownEnd = intervals[0][1]
        overlapRes = 0

        for start, end in intervals[1:]:
            if start < lastKnownEnd:
                overlapRes += 1
                if end <= lastKnownEnd:
                    lastKnownEnd = end
            else:
                lastKnownEnd = end
        return overlapRes
