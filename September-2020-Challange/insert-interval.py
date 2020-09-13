'''
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3458/
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n=len(intervals)
        if n==0:
            return [newInterval]
        l=0
        r=n-1
        
        while(l<n and newInterval[0]>intervals[l][1]):
            l+=1
        
        if (l==n-1 and intervals[l][1]<newInterval[0]) or l==n:
            intervals.append(newInterval)
            return intervals
        
        while(newInterval[1]<intervals[r][0] and r>=0):
            r-=1
            
        if r<0:
            intervals=[newInterval]+intervals
            return intervals

        return (intervals[0:l]+[[intervals[l][0],max(newInterval[1],intervals[r][1])]]+intervals[r+1:])
