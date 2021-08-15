'''
https://leetcode.com/problems/set-matrix-zeroes/
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        minRow = -1<<32
        minCol = minRow-1
        minBoth = minCol - 1
        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] ==0 :
                    if matrix[i][0]==minCol or matrix[i][0]==minBoth: matrix[i][0] = minBoth
                    else: matrix[i][0] =minRow
                    if matrix[0][j]==minRow or matrix[0][j]==minBoth: matrix[0][j] = minBoth
                    else: matrix[0][j]=minCol
        for i in range(m):
            if matrix[i][0]==minRow or matrix[i][0] == minBoth:
                for j in range(n):
                    if matrix[i][j]>minRow: matrix[i][j]=0
        for j in range(n):
            if matrix[0][j] == minCol or matrix[0][j] == minBoth:
                for i in range(m):
                    matrix[i][j]=0
        
        for i in range(m):
            if matrix[i][0]<=minRow:
                matrix[i][0]=0
        
