class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        sx, sy, ex, ey, ec = 0, 0, 0, 0, 1
        m = len(grid)
        n = len(grid[0])
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    sx, sy = x, y
                elif grid[x][y] == 2:
                    ex, ey = x, y
                elif grid[x][y] == 0:
                    ec += 1
        
        def dfs(x, y, rem):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == -1:
                return 0
            if (x, y) == (ex, ey):
                return 1 if rem == 0 else 0
            
            grid[x][y] = -1
            total_paths = (dfs(x + 1, y, rem - 1) +
                           dfs(x, y + 1, rem - 1) +
                           dfs(x - 1, y, rem - 1) +
                           dfs(x, y - 1, rem - 1))
            grid[x][y] = 0
            
            return total_paths
        
        return dfs(sx, sy, ec)