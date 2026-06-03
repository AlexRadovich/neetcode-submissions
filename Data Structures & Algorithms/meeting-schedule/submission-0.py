"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        interval = []
       
            
        interval = sorted(intervals,key = lambda x:x.start)
        interval = sorted(interval,key = lambda x:x.end)
        fast = 0

        for i in interval:
            print(i.start,i.end)

        for i in interval:
            if i.start < fast:
                print("here", i.start,fast)
                return False
            else:
                fast = i.end
        return True

