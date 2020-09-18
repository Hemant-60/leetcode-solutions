'''
https://leetcode.com/problems/climbing-stairs/
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:return 1
        if n==2:return 2
        prev1,prev2=1,2
        for i in range(3,n):
            temp=prev2+prev1
            prev1,prev2=prev2,temp
        return prev1+prev2
