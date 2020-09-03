'''
https://leetcode.com/problems/repeated-substring-pattern/
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        factors=[]
        ls=len(s)
        for i in range(1,ls//2 +1):
            if(ls%i==0):
                factors.append(i)

        for i in factors:
            if(s[0:i]*(ls//i)==s):
                return True
        
        return False
