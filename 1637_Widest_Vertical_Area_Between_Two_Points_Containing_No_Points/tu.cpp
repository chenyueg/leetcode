class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        vector<int> xz(points.size(), 0);
        for(int i=0;i<points.size();i++)
        {
            xz[i] = points[i][0];
        }
        std::sort(xz.begin(), xz.end());
        int max_width = 0;
        for(int i=1;i<xz.size();i++)
        {
            if(xz[i] - xz[i-1] > max_width)
            {
                max_width = xz[i] - xz[i-1];
            }
        }
        return max_width;
    }
};