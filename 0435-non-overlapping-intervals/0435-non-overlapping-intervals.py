class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        answer = 0
        intervals = sorted(intervals, key= lambda x: x[1])
        cs, ce = intervals[0]
        for i in range(1, len(intervals)):
            ns, ne = intervals[i]
            if cs <= ns < ce or ns <= cs or ne <= ce:
                answer +=1
            else:
                ce = ne
            
        return answer
            
           
