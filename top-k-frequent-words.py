'''
https://leetcode.com/problems/top-k-frequent-words/
'''
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for i in words:
            if i in d: d[i]+=1
            else: d[i]=1
        d2={i:[] for i in sorted(set([j for j in d.values()]),reverse=True)} 
        for i in d:d2[d[i]].append(i)
        for i in d2:d2[i].sort()
        vals=[]
        for i in d2:
            ld=len(d2[i])
            for j in range(0,min(ld,k)):
                vals.append(d2[i][j])
            k-=ld
            if k<=0: return vals
        return vals
