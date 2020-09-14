'''
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3459/
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        
        if n==0: return 0
        if n==1: return nums[0]
        if n==2: return max(nums)
        
        ms=[0 for i in range(0,n)]
        ms[0]=nums[0]
        ms[1]=max(nums[1],nums[0])
        
        for i in range(2,n):
            ms[i]=max(ms[i-1],nums[i]+ms[i-2])
        
        return ms[n-1]
            
            
