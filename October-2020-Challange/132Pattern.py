'''
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3505/
'''
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<3: return False
        min_left=nums[0]
        for i in range(1,n-1):
            if nums[i]>min_left:
                for j in range(i+1,n):
                    if nums[j]<nums[i] and nums[j]>min_left:
                        return True
            
            min_left= min(min_left, nums[i])
        
        return False
