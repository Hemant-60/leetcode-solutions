'''
https://leetcode.com/problems/zigzag-conversion/
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows==1: return s
        l=[[] for i in range(0,numRows)]
        
        count=0
        r=0
        for i in s:
            if count==(numRows-1):
                r=1
            if count==0:
                r=0
                
                
            if r==0:
                l[count].append(i)
                count+=1
            if r==1:
                l[count].append(i)
                count-=1
                
        print(l)
        s=""
        for i in l:
            for k in i:
                s+=k
        return s
