'''
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3454/
'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1l=[int(i) for i in version1.split(".")]
        v2l=[int(i) for i in version2.split(".")]
        
        l1,l2=len(v1l),len(v2l)
        
        for i in range(min(l1,l2)):
            if v1l[i]>v2l[i]:
                return 1
            elif v1l[i]<v2l[i]:
                return -1
        
        if l1>l2:
            for i in range(l2,l1):
                if(v1l[i]>0):
                    return 1

        elif l1<l2:
            for i in range(l1,l2):
                if(v2l[i]>0):
                    return -1
        
        
        return 0
        
