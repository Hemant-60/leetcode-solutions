from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = deque()
        for i in asteroids:
            if True:
                if True:
                    flag=0
                    while stk and (stk[-1] <=abs(i)) and (stk[-1]>0 and i<0):
                        k = stk.pop()
                        if k==abs(i):
                            flag=1
                            break
                    if flag==0:
                        if not stk or stk[-1]<abs(i): stk.append(i)
                else:
                    stk.append(i)
        return stk
