class Solution {
public:
    int sumOfMultiples(int n) {
        int result = 0;
        vector<int> plus_list = {3,5,7,105};
        for(int i: plus_list)
        {
            result += (i+n/i*i)*(n/i)/2;
        }
        vector<int> minus_list = {15, 21, 35};
        for(int i: minus_list)
        {
            result -= (i+n/i*i)*(n/i)/2;
        }
        return result;
    }
};