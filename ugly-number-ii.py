'''
https://leetcode.com/problems/ugly-number-ii/
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n in range(1,7): return n
        d=[1]
        count=0
        x,y,z=0,0,0
        while(count<n):
            count+=1
            d.append(min(d[x]*2,d[y]*3,d[z]*5))
            c=d[-1]
            if c==d[x]*2: x+=1
            if c==d[y]*3: y+=1
            if c==d[z]*5: z+=1
        return d[-2]
