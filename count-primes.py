'''
https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/744/
'''
class Solution:
    
    def fillSieve(self,sieve,n,limit):
        tn=n*n
        while(tn<limit):
            sieve[tn-1]=1
            tn+=n
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1: return 0
        sieve=[0 for i in range(0,n)]
        count=0
        for i in range(2,n):
            if sieve[i-1]==0:
                count+=1
                self.fillSieve(sieve,i,n)
        
        return count
