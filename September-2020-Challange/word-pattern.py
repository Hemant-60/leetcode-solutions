'''
https://leetcode.com/problems/word-pattern/
'''

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        sp=set([i for i in pattern])
        k=str.split(" ")
        ss=set(k)
        
        if len(sp)==len(ss) and len(pattern)==len(k):
            d={}
            for i in range(0,len(pattern)):
                
                if(pattern[i] not in d):
                    if(k[i] not in ss):
                        return False
                    d[pattern[i]]=k[i]
                    ss.discard(k[i])
                else:
                    if(d[pattern[i]]!=k[i]):
                        return False
            
            return True
        else:
            return False
        
