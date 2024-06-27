class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ones_rows = [sum(row) for row in grid]
        ones_cols = [sum([row[i] for row in grid]) for i in range(len(grid[0]))]
        # print(ones_rows)
        # print(ones_cols)
        result = []
        for i in range(len(grid)):
            result.append([0] * len(grid[0]))
            # print(result)
            for j in range(len(grid[0])):
                result[i][j] = ones_rows[i] + ones_cols[j] - (len(grid) - ones_rows[i]) - (len(grid[0]) - ones_cols[j])
        return result
