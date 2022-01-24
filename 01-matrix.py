class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        cost = [[float('inf') for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    if i-1 >=0: cost[i][j] = min(cost[i][j], cost[i-1][j] + 1)
                    if j-1 >=0: cost[i][j] = min(cost[i][j], cost[i][j-1] + 1)
                else: cost[i][j]=0
                    
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if mat[i][j]==1:
                    if i+1 < m: cost[i][j] = min(cost[i][j], cost[i+1][j] + 1)
                    if j+1 < n: cost[i][j] = min(cost[i][j], cost[i][j+1] + 1)
                else: cost[i][j]=0
        
        return cost
    
        
