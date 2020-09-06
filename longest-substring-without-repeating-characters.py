'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = len(s)
        d = {}
        mcount = 0
        curr = 0
        if (s == ""): return 0
        r=0
        while (r < ls):
            # print("here")
            if s[r] not in d:
                d[s[r]] = r
                curr += 1
            else:
                r = d[s[r]] + 1
                d = {}
                d[s[r]] = r
                mcount = max(curr, mcount)
                curr = 1
            r += 1

        return max(mcount, curr)
                    
        
