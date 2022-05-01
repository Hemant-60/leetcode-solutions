class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3: return max(nums)
        n = len(nums)
        def solve(vals, n):
            p1, p2 = max(vals[1], vals[0]), vals[0]
            curr  = p2 
            for i in range(2,n):
                curr = max(p2+vals[i], p1)
                p2 = p1
                p1 = curr
            return p2
        
        return max(solve(nums, n), solve(nums[::-1], n))
