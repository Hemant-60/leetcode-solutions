'''
https://leetcode.com/problems/3sum-closest/
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        minDiff = 3001
        minSum = sum(nums[:3])
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                currSum = nums[i]+nums[l]+nums[r]
                if currSum > target:r-=1
                else: l+=1
                    
                if minDiff>abs(currSum-target):
                    minDiff = abs(currSum-target)
                    minSum = currSum
        return minSum
