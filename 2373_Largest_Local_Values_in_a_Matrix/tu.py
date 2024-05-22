class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(grid) - 2):
            result.append([])
            for j in range(len(grid[i]) - 2):
                _max = 0
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        _max = max(_max, grid[x][y])
                result[-1].append(_max)
        return result