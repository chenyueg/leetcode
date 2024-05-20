class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        vector<vector<int>> result(grid.size()-2, vector<int>(grid[0].size()-2, 0));
        for(int i=0;i<grid.size()-2;i++)
        {
            for(int j=0;j<grid[i].size()-2;j++)
            {
                int _max = 0;
                for(int x=i;x<=i+2;x++)
                {
                    for(int y=j;y<=j+2;y++)
                    {
                        if(_max < grid[x][y])
                        {
                            _max = grid[x][y];
                        }
                    }
                }
                result[i][j] = _max;
            }
        }
        return result;
    }
};