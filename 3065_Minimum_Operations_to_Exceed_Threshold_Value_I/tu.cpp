class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int result = 0;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i] <k)
            {
                result += 1;
            }
        }
        return result;
    }
};