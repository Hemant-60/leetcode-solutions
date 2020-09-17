'''
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3463/
'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        instructions*=4
        x,y=0,0
        d=0
        for i in instructions:
            if i=="G":
                if d==0:
                    y+=1
                elif d==1:
                    x+=1
                elif d==2:
                    y-=1
                else:
                    x-=1
            elif i=="L":
                d= 3 if d==0 else (d-1)
            else:
                d= 0 if d==3 else (d+1)

            
        if x==0 and y==0 and d==0:
                return True
            
        return False               
