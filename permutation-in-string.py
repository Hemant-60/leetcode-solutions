from collections import deque
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        c1 = [0 for i in range(26)]
        c2 = [0 for i in range(26)]
        for i in s1:
            c1[ord(i)-ord('a')]+=1
        for i in range(len(s1)):
            c2[ord(s2[i]) - ord('a')]+=1
        
        for i in range(len(s2)-len(s1)+1):
            if c1==c2: return True
            c2[ord(s2[i])-ord('a')]-=1
            if (i+len(s1)>=len(s2)): break
            c2[ord(s2[i+len(s1)]) - ord('a')]+=1
        
        return False
