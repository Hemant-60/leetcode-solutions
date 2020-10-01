'''
https://leetcode.com/explore/featured/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3480/
'''

class RecentCounter:

    def __init__(self):
        self.vals=[]

    def ping(self, t: int) -> int:
        self.vals.append(t)
        if self.vals!=[]:
            while self.vals[0]<(t-3000) and self.vals!=[]:
                self.vals.pop(0)
            return len(self.vals)
            


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
