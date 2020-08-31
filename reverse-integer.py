'''
Author : Hemant Rana
Date : 30th Aug 2020
link : https://leetcode.com/problems/reverse-integer
'''

class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        num2 = 0

        while (num != 0):
            num2 *= 10
            num2 += num % 10
            num //= 10

        if (x < 0):
            num2 *= -1

        if(num2>(-2**31) and num2<(2**31-1)):
            return num2
        else:
            return 0
                
        
        
