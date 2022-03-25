class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key = lambda x: -abs(x[0]-x[1]))
        a = b = len(costs)//2
        c = 0
        print(costs)
        for i in range(a+b):
            if a>0 and (costs[i][0]<costs[i][1] or b ==0):
                c+=costs[i][0]
                a-=1
            else:
                b-=1
                c+=costs[i][1]
        return c
