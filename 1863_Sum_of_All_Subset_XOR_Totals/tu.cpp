class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        vector<int> result;
        for(int i=0;i<nums.size();i++)
        {
            int length = result.size();
            for(int j=0; j<length; j++)
            {
                result.push_back(result[j] ^ nums[i]);
            }
            result.push_back(nums[i]);
        }
        return accumulate(result.begin(), result.end(), 0);
    }
};