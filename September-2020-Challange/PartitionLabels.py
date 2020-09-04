'''
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3448/
'''

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        ls=len(S)
        l=0
        r=0
        if(ls==1):
            return [1]
        
        last={chr(ord('a')+i):0 for i in range(0,26)}
        
        for i in range(ls-1,0,-1):
            if(i>last[S[i]]):
                last[S[i]]=i
        indices=[]
        start=0
        mxi=-1
        for i in range(0,ls):
            mxi=max(last[S[i]],mxi)
            
            if mxi==i:
                indices.append(i-start+1)
                start=i+1
                
        return indices
