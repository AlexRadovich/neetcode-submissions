class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)

        if len(intervals) == 1: return intervals
        if not intervals: return []

        
        ret = []

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(len(intervals)):
            
            if len(ret) == 0:
                ret.append(intervals[i])
                continue
            top = ret.pop()
            if intervals[i][0] <= top[1]:
                ret.append([top[0], max(top[1],intervals[i][1]) ])
            else:
                ret.append(top)
                ret.append(intervals[i])



        
        return ret
            


