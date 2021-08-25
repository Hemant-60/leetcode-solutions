#With Binary Search

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def isPerfectSquare(num):
            if num==1: return True
            l,r=2,num
            while l<=r:
                m=(l+r)//2
                if m*m == num: return True
                elif m*m < num: l=m+1
                else: r=m-1
            return False
            
        srt =int(sqrt(c))
        for i in range(srt+1):
            sq = i*i
            if 2*sq == c or isPerfectSquare(c - sq) is True: return True
        return False
    
    
#With sqrt function

from math import sqrt,ceil
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def isPerfectSquare(num):
            return sqrt(num)%1==0
            
        srt =int(sqrt(c))
        for i in range(srt+1):
            sq = i*i
            if 2*sq == c or isPerfectSquare(c - sq) is True: return True
        return False
