class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        int result = 0;
        int left = 0;
        int right = nums.size() - 1;
        sort(nums.begin(), nums.end());
        while(left < right)
        {
            if(nums[left] + nums[right] < target)
            {
                result += right - left;
                left += 1;
            }
            else
            {
                right -= 1;
            }
        }
        return result;
    }
};