class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        onesRow= [sum(row) for row in grid] 
        onesCol= [sum(row[j] for row in grid) for j in range(n)]
        diff = [[0] * n for k in range(m)]
        for i in range(m):
            for j in range(n):
                zerosRow= n-onesRow[i]
                zerosCol= m-onesCol[j]
                diff[i][j]=onesRow[i]+onesCol[j]-zerosRow-zerosCol
        return diff