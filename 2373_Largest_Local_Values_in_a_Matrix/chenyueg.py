class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid) - 2
        result = []
        for i in range(n):
            row = []
            for j in range(n):
                sub = [grid[x][j:j+3] for x in range(i,i+3)]
                maxsub = max(max(each) for each in sub)
                row.append(maxsub)
            result.append(row)
        return result