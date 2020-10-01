'''
https://leetcode.com/problems/longest-valid-parentheses/
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        maxValid=0
        for i in range(0,len(s)):
            if s[i]=="(": stack.append(i)
            else:
                stack.pop()
                if stack==[]: stack.append(i)
                else: maxValid=max(maxValid,i-stack[-1])
        return maxValid
