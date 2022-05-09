class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = {"()"}
        for i in range(1, n):
            res = set()
            for j in dp:
                for k in range(2*(i+1)):
                    res.add(j[0:k]+"()"+j[k:])
                    
            dp = res
        
        return dp
