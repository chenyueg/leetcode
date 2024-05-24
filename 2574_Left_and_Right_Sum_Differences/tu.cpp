class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        vector<int> result(nums.size(), 0);
        int left = 0;
        int right = accumulate(nums.begin(), nums.end(), 0);
        int previous = 0;
        for(int i=0;i<nums.size();i++)
        {
            left += previous;
            right -= nums[i];
            result[i] = abs(left - right);
            previous = nums[i];
        }
        return result;
    }
};