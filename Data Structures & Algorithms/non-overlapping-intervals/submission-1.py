class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)

        count = 0

        end = intervals[0][1]
        print(intervals)

        for ix, val in enumerate(intervals[1:]):
            if val[0] < end:
                end = min(val[1],end)
                count += 1
            else:
                end = val[1]

        return count