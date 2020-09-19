'''
https://leetcode.com/explore/featured/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3465/
'''
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s="123456789"
        nums=[]
        for i in range(0,9):
            for j in range(0,9-i):
                nums.append(int(s[j:j+i+1]))
        l,r=0,len(nums)-1
        f0,f1=0,0
        while(l<=r):
            if nums[l]<low: l+=1
            else: f0=1
            if nums[r]>high:r-=1
            else: f1=1

            if f1==1 and f0==1: break
        return nums[l:r+1]
