class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());

        vector<int> u_nums(1,nums[0]);
        vector<int> u_nums_count(1,1);
        for(int i=1;i<nums.size();i++)
        {
            if(nums[i]==nums[i-1])
            {
                u_nums_count.back() += 1;
            }
            else
            {
                u_nums.push_back(nums[i]);
                u_nums_count.push_back(1);
            }
        }

        int max_count = *std::max_element(u_nums_count.begin(), u_nums_count.end());
        vector<vector<int>> result(max_count, vector<int>(0));

        for(int i=0; i<u_nums.size(); i++)
        {
            for(int j=0; j<u_nums_count[i]; j++)
            {
                result[j].push_back(u_nums[i]);
            }
        }

        return result;
    }
};