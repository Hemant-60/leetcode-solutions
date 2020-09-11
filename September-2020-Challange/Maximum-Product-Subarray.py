'''
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3456/
'''
class Solution:
    
    def hasNegative(self,nums, s, e):
        for i in range(s,e):
            if(nums[i]==0):
                return False
            elif(nums[i]<0):
                return True
        return False
    
    def mxProd(self,nums):
        maxP=-10**7
        n=len(nums)
        prod=-10**7
        for i in range(0,n):
            if(nums[i]==0):
                maxP=max(maxP,prod,0)
                prod=-10**7
            elif(nums[i]<0 and prod>0):
                if(self.hasNegative(nums,i+1,n)):
                    if prod == -10**7:
                        prod=1
                    prod*=nums[i]
                else:
                    maxP=max(prod,maxP)
                    prod=-10**7
            else:
                if prod==-10**7:
                    prod=1
                prod*=nums[i]
        
        return max(maxP,prod)
    
    def maxProduct(self, nums: List[int]) -> int:
        k=self.mxProd(nums)
        nums.reverse()
        
        return max(self.mxProd(nums),k)
