'''
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3461/
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s=="": return 0
        count=0
        for i in s[::-1]:
            if i==" ":
                if count!=0:
                    return count
            else:
                count+=1
        return count
