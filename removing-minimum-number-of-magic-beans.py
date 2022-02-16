class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        s = sum(beans)
        beans.sort()
        smaller=0
        minCost = float('inf')
        n = len(beans)
        for i in range(n):
            s-=beans[i]
            currCost = s-(beans[i]*(n-i-1)) + smaller
            minCost = min(minCost, currCost)
            smaller+=beans[i]
        
        return minCost
