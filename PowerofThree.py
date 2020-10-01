'''
https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/745/
'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        from math import log
        return False if n<=0 else 3**(math.ceil(log(n)/log(3)))==n
