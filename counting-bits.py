'''
https://leetcode.com/problems/counting-bits/
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        if num==0: return [0]
        if num==1: return [0,1]
        from math import log2
        dp=[0,1,1]+[0 for i in range(3,num+1)]
        count=2
        for i in range(3,num+1):
            if log2(i)%1==0:
                count=i
            dp[i]=dp[i-count]+1
        print(dp)
        return dp
