'''
https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/878/
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        v=[["I","V","X","L","C","D","M"],[1,5,10,50,100,500,1000]]
        ls=len(s)
        year=0
        i=0
        while(i<ls):
            if i<(ls-1) and s[i] in v[0][0:v[0].index(s[i+1])]:
                year+=(v[1][v[0].index(s[i+1])]-v[1][v[0].index(s[i])])
                i+=2
            else:
                year+=v[1][v[0].index(s[i])]
                i+=1
        
        return year
