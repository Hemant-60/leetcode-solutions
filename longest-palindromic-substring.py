'''
https://leetcode.com/problems/longest-palindromic-substring/
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if(n==0 or n==1 or (n==2 and s[0]==s[1])): return s
        if n==2: return s[0]
        max_len=0
        max_str=""
        for i in range(0,n):
            l,r=0,0
            
            if(i>0 and s[i-1]==s[i]):
                # print(1)
                l=i-1
                r=i
                while(True):
                    if((l-1)>=0 and (r+1)<n and s[l-1]==s[r+1]):
                        l-=1
                        r+=1
                    else:
                        break
                if(r-l)>max_len:
                    max_str=s[l:r+1]
                    max_len=max(r-l,max_len)
            
            if(i<n-1 and s[i]==s[i+1]):
                # print(2)
                l=i
                r=i+1
                while(True):
                    if((l-1)>=0 and (r+1)<n and s[l-1]==s[r+1]):
                        l-=1
                        r+=1
                    else:
                        break
                if(r-l)>max_len:
                    max_str=s[l:r+1]
                    max_len=max(r-l,max_len)
            if True:
                if(i>0 and i<n-1 and s[i-1]==s[i+1]):
                    # print(3)
                    l=i-1
                    r=i+1
                    while(True):
                        if((l-1)>=0 and (r+1)<n and s[l-1]==s[r+1]):
                            l-=1
                            r+=1
                        else:
                            break
                    
                    if(r-l)>max_len:
                        max_str=s[l:r+1]
                        max_len=max(r-l,max_len)
            # print(max_len,max_str)
        if max_str=="" and n>0:
            max_str=s[0]
        return max_str           
