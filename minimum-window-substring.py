from collections import Counter
class Solution:
    def compare(self, tset, curr):
        for i in tset:
            if curr[i]< tset[i]: return False
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        if s==t: return s
        if len(t)>len(s): return ""
        ind = []
        tset = Counter(t)
        curr = {i:0 for i in t}
        for i, val in enumerate(s):
            if val in tset:
                ind.append((val,i))
       
        if ind==[]: return ""
        minStr=""
        minLen = float('inf')
        l,r =0,0
        curr[ind[l][0]]+=1
        while r<len(ind):
            if not self.compare(tset,curr):
                r+=1
                if r==len(ind): break
                curr[ind[r][0]]+=1
            else:
                if (ind[r][1]-ind[l][1]+1)<minLen:
                    minLen = ind[r][1]-ind[l][1]+1
                    minStr = s[ind[l][1]:ind[r][1]+1]
                curr[ind[l][0]]-=1
                l+=1
        return minStr
