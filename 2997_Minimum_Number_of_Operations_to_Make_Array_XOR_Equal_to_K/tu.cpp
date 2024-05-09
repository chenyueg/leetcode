class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int out = k;
        for(int i=0;i<nums.size();i++)
        {
            out ^= nums[i];
        }
        int count = 0;
        while(out)
        {
            count += out & 1;
            out >>= 1;
        }
        return count;
    }
};