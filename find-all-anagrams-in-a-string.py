from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s): return []
        res=[]
        curr= Counter(s[:len(p)])
        pc = Counter(p)
        if curr==pc: res.append(0)
        for i in range(1,len(s)-len(p)+1):
            curr[s[i-1]]-=1
            if curr[s[i-1]]==0:
                del curr[s[i-1]]
            if s[i-1+len(p)] in curr:
                curr[s[i-1+len(p)]]+=1
            else:
                curr[s[i-1+len(p)]] = 1
            if curr == pc:
                res.append(i)
        return res
            
            
        
