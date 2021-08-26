from collections import deque
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        mins = deque([arr[-1]]) #[arr[-1] for i in range(n)]
        maxs=arr[0]
        c=0
        for i in range(n-2,-1,-1): mins.appendleft(min(arr[i],mins[0]))
        for i in range(n-1):
            maxs = max(maxs,arr[i])
            if maxs<=mins[i+1]:c+=1
        return min(c+1,n)
