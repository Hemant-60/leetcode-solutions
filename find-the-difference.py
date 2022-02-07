class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor_sum=0
        for i in range(len(s)):
            xor_sum^=ord(s[i])
            xor_sum^=ord(t[i])
        xor_sum^=ord(t[-1])
        
        return chr(xor_sum)
