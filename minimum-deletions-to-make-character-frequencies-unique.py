class Solution:
    def minDeletions(self, s: str) -> int:
        count=[0 for i in range(26)]
        for i in s: count[ord(i)-ord('a')]+=1
        count=[i for i in count if i>0]
        count.sort(reverse=True)
        mx = max(count)
        values=0
        mn=count[0]
        for i in range(1,len(count)):
            if mn<=count[i]:
                mn=max(mn-1,0)
                values+=(count[i]-mn)
            else: mn = count[i]
        return values
