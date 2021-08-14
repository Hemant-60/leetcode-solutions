'''
https://leetcode.com/problems/jump-game/
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j = len(nums)
        mx_pos = nums[0]
        for i in range(j-1):
            mx_pos = max(nums[i]+i, mx_pos)
            if mx_pos>=(j-1): return True
            if i==mx_pos and nums[i]==0: return False
        return True
