class Solution:
    def summaryRanges(self, num: List[int]) -> List[str]:
        res=[]
        curr=[0,-1]
        num.append(2**31+3)
        for i in range(1,len(num)):
            if num[i] == ((i-curr[0])+num[curr[0]]):
                curr[1]=i
            else:
                if curr[1]==-1:
                    res.append("{}".format(num[curr[0]]))
                else:
                    res.append("{}->{}".format(num[curr[0]], num[curr[1]]))
                curr[0] = i
                curr[1]=-1
            
        return res
