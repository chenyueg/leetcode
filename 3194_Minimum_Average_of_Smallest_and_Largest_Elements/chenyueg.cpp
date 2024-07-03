class Solution {
public:
    double minimumAverage(vector<int>& nums) 
    {
        int n = nums.size();
        std::sort(nums.begin(), nums.end());
        double minAvg = (nums[0] + nums[n - 1]) / 2.0;

        for (int i = 1; i < n / 2; ++i) 
        {
            double avg = (nums[i] + nums[n - 1 - i]) / 2.0;
            if (avg < minAvg) 
            {
                minAvg = avg;
            }
        }

        return minAvg;
    }
};