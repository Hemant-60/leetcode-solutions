'''
https://leetcode.com/problems/longest-palindromic-substring/
'''

class Solution:
    
    def isPalindrome(self, s, n):
        if n%2==0:
            if(s[0:n//2]==s[n-1:n//2 - 1:-1]): return True
        elif n%2!=0:
            if(s[0:n//2]==s[n-1:n//2:-1]): return True
        
        return False
    
    def longestPalindrome(self, s: str) -> str:
        ls=len(s)
        count=0
        if s=="": return ""
        lp=s[0]
        for i in range(0,ls):
            for j in range(i+1,ls):
                if s[i]==s[j]:
                    if self.isPalindrome(s[i:j+1],j-i+1):
                        if(j-i+1)>count:
                            lp=s[i:j+1]
                            count=j-i+1
        
        return lp
                
