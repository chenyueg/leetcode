class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for each in range(m)]
        i, j = m - 1, n - 1
        
        while i >= 0 and j >= 0:
            if rowSum[i] <= colSum[j]:
                matrix[i][j] = rowSum[i]
                colSum[j] -= rowSum[i]
                i -= 1
            else:
                matrix[i][j] = colSum[j]
                rowSum[i] -= colSum[j]
                j -= 1
        
        return matrix