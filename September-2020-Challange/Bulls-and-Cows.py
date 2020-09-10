'''
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3455/
'''
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A,B=0,0
        sl={}
        gl={}
        for i in range(0,len(secret)):
            if(secret[i]==guess[i]): A+=1
            else:
                if secret[i] in sl:
                    sl[secret[i]]+=1
                elif secret[i] not in sl:
                    sl[secret[i]]=1
                    
                if guess[i] in gl:
                    gl[guess[i]]+=1
                elif guess[i] not in gl:
                    gl[guess[i]]=1
        
        for i in sl:
            if i in gl:
                B+=min(sl[i],gl[i])
        
        return str(A)+"A"+str(B)+"B"
