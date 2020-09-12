'''
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3457/
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k>n or k>9: return []
        
        if sum([i for i in range(10-k,10)])<n:
            return []
        if sum([i for i in range(10-k,10)])==n:
            return [[i for i in range(10-k,10)]]
        
        import itertools
        subsets= list(itertools.combinations([i for i in range(1,10)], k))
        res=[]
        for i in subsets:
            if sum(i)==n:
                res.append(i)
        return res
