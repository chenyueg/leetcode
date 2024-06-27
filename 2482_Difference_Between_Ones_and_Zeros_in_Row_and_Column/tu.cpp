class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        int r = grid.size();
        int c = grid[0].size();
        vector<int> rows(r);
        vector<int> cols(c);
        vector<vector<int>> result(r, vector<int>(c,0));
        for(int i = 0; i < r; i++)
        {
            rows[i] = accumulate(grid[i].begin(), grid[i].end(), 0);
            for(int j=0; j < c; j++)
            {
                cols[j] += grid[i][j];
            }
        }

        for(int i = 0; i < r; i++)
            for(int j=0; j < c; j++)
            {
                result[i][j] = 2 * rows[i] + 2 * cols[j] - r - c;
            }
        return result;
    }
};