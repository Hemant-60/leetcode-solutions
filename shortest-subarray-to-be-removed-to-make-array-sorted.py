'''
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
'''
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n=len(arr)
        if n==0 or n==1: return 0
        l=0
        r=n-1
        for i in range(0,n-1):
            if arr[i]<=arr[i+1]:
                l+=1
            else:
                break
        
        if l==(n-1): return 0
        
        while(r>0):
            if arr[r]>=arr[r-1]:
                r-=1
            else:
                break
        if l==0 and r==n-1:
            if arr[l]<=arr[r]:
                return n-2
            return n-1
        
        mx=max(l+1,n-r)
        tl=0
 
        while(tl<=l):
            count=0
            while(arr[tl]==arr[tl+1]):
                tl+=1
            
            count+=tl
            while(r<(n) and arr[tl]>arr[r] ):
                if r==n: break
                r+=1
            count+=(n-r+1)
            mx=max(mx,count)
            tl+=1
        print(mx)
        return n-mx
