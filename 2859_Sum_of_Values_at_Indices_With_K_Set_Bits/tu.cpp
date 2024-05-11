class Solution {
public:
    int countBit(int n)
    {
        int result = 0;
        while(n)
        {
            result += n& 1;
            n >>= 1;
        }
        return result;
    }


    int sumIndicesWithKSetBits(vector<int>& nums, int k) {
        int result = 0;
        for(int i=0;i<nums.size();i++)
        {
            if(countBit(i) == k)
            result += nums[i];
        }
        return result;
    }
};