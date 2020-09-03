'''
https://leetcode.com/problems/contains-duplicate-iii/
'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    
        n=len(nums)
        if (k == 0 or n==0 or n==1 or (t==0 and len(set(nums))==n)):
            return False
        
        for i in range(0,n):
            for j in range(i+1,i+k+1):
                if j<n and abs(nums[i]-nums[j])<=t:
                    return True
        
        return False
        

