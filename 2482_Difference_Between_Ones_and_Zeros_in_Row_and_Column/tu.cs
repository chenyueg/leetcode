public class Solution {
    public int[][] OnesMinusZeros(int[][] grid) {
        int r = grid.Length;
        int c = grid[0].Length;
        int[] rows = new int[r];
        int[] cols= new int[c];
        int[][] result = new int[r][];
        for(int i = 0; i < r; i++)
        {
            result[i] = new int[c];
            for(int j=0; j < c; j++)
            {
                cols[j] += grid[i][j];
                rows[i] += grid[i][j];
            }
        }

        for(int i = 0; i < r; i++)
            for(int j=0; j < c; j++)
            {
                result[i][j] = 2 * rows[i] + 2 * cols[j] - r - c;
            }
        return result;
    }
}