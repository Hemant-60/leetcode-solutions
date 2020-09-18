'''
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3464
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n==0 or n==1: return 0
        profit=0
        minNum=prices[0]
        for i in range(1,n):
            profit=max(profit,prices[i]-minNum)
            minNum=prices[i] if prices[i]<minNum else minNum

        return profit 
