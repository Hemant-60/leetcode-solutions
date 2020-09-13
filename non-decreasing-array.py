'''
https://leetcode.com/problems/non-decreasing-array/
'''

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count=0
        n=len(nums)
        if n==0 or n==1 or n==2: return True
        j=0
        mx=nums[0]
        
        c=0
        for i in range(1,n):
            if mx>nums[i]:
                c+=1
            else:
                mx=max(mx,nums[i])
            if c>1:
                break
        if c==1: return True
            
        
        while(j<(n-1)):
            if nums[j]>nums[j+1]:
                nums[j]=nums[j+1]
                count+=1
                if j>0:
                    mx=max(nums[j-1],nums[j+1])
                else:
                    mx=nums[j+1]
                break
            j+=1
            
        if j>=(n-2):
            
            return True
        for i in range(j,n):
            
            if nums[i]<mx:
                count+=1
            if count>=2:
                return False
            mx=max(mx,nums[i])
        
        return True
