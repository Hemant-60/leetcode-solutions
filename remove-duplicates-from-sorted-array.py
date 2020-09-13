'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(nums==[]):
            return 0
        length=1
        cnum=nums[0]
        ci=0
        for i in range(1,len(nums)):
            if(cnum!=nums[i]):
                # print(here)
                length+=1
                cnum=nums[i]
                nums[length-1]=cnum
                # ci+=1

        return length
            
