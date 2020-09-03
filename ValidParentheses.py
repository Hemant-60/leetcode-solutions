'''
https://leetcode.com/problems/valid-parentheses/
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={"(":")","{":"}","[":"]"}
        for i in s:
            if (i in d):
                stack.append(i)
            else:
                if(stack==[]):
                    return False
                k=stack.pop()
                if(d[k]!=i):
                    return False

        if(stack==[]):
            return True
        else:
            return False
