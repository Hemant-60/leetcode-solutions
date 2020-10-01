'''
https://leetcode.com/problems/k-closest-points-to-origin/
'''
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        d={}
        for i in points:
            curr_d=(i[0]**2 + i[1]**2)
            if curr_d in d: d[curr_d].append(i)
            else: d[curr_d]=[i]
        vals=[]
        while(True):
            for i in sorted(d):
                for j in d[i]:
                    vals.append(j)
                    K-=1
                    if K==0: return vals 
