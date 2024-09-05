class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dr = 0
        dc = 1
        n = 0 #
        result = []

        r = rStart
        c = cStart

        while(len(result) < rows * cols):
            for i in range(n//2+1): #
                if 0<=r<rows and 0<=c<cols:
                    result.append([r,c])
                r += dr
                c += dc
            dr, dc = dc, -dr #
            n += 1  #
        return result

