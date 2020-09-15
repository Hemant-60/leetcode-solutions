'''
https://leetcode.com/problems/find-the-town-judge/
'''
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if trust==[]:
            return 1 if N==1 else -1
        t1=set()
        t2=set()
        t=[0 for i in range(0,N)]
        
        for i in trust:
            t1.add(i[0])
            t2.add(i[1])
            t[i[1]-1]+=1
        
        k=t2.difference(t1)
        if len(k)!=1:
            return -1
        val=k.pop()
        
        if t[val-1]==(N-1):
            return val
        return -1
