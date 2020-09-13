'''
https://leetcode.com/problems/max-points-on-a-line/
'''
class Solution:
    
    def maxPoints(self, points: List[List[int]]) -> int:
        
        lp=len(points)
        if lp==0: return 0
        if lp==1:
            return 1
        if lp==2:
            return 2
        max_points=0
        for i in range(0,lp-1):
            dp={}
            k=0
            for j in range(i+1,lp):
                if points[i]==points[j]:
                    k+=1
                else:
                    if (points[j][0]-points[i][0]) == 0:
                        slope=None
                    else:
                        slope=(points[j][1]-points[i][1])/(points[j][0]-points[i][0])

                    if slope in dp:
                        dp[slope]+=1
                    else:
                        dp[slope]=2
                    # print(i,slope)
            if dp=={}:
                max_points=max(max_points,k+1)
            else:
                max_points=max(max_points,max(dp.values())+k)
            # print(max_points,dp)
        return max_points
