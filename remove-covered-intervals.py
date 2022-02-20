class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count=len(intervals)
        
        def enclose(i,j):
            return True if i[0]<=j[0] and j[1]<=i[1] else False
        
        for i in range(1, len(intervals)):
            if enclose(intervals[i-1],intervals[i]):
                intervals[i] = intervals[i-1]
                count-=1
            elif enclose(intervals[i],intervals[i-1]):
                intervals[i-1] = intervals[i]
                count-=1
        return count
