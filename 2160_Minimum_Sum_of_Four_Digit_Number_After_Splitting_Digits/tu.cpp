class Solution {
public:
    int minimumSum(int num) {
        int pos = 0;
        string nums = to_string(num);
        vector<string> results{"", ""};
        sort(nums.begin(), nums.end());
        reverse(nums.begin(), nums.end());
        for(int i = nums.length()-1; i>=0; i--)
        {
            results[pos].append(1, nums[i]);
            // nums[i] is char, so calling append(size_type count, CharT ch) and 1 is necessary
            pos = 1 - pos;
        }
        return stoi(results[0]) + stoi(results[1]);
    }
};