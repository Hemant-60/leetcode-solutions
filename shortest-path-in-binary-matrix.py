from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n==1: return -1 if grid[0][0] == 1 else 1
        if grid[0][0]==1 or grid[n-1][n-1] == 1: return -1
        for i in range(n):
            for j in range(n):
                grid[i][j]^=1
                if grid[i][j] == 1:
                    grid[i][j] = float('inf')
        grid[0][0] = 1
        q = deque([(0,0)])
        
        while q:
            i, j = q.popleft()
            coor = [(i-1, j-1), (i-1,j), (i-1, j+1), (i,j-1), (i, j+1), (i+1,j-1),(i+1,j), (i+1,j+1)]
            
            for c in coor:
                if c[0]<n and c[0]>=0 and c[1]<n and c[1]>=0:
                    if grid[c[0]][c[1]] == float('inf'):
                        grid[c[0]][c[1]] = grid[i][j]+1
                        q.append((c[0],c[1]))
        return -1 if grid[n-1][n-1] == float('inf') else grid[n-1][n-1]
