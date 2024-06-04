class Solution {
public:
    int numberOfMatches(int n) {
        int result = 0;
        while(n > 1)
        {
            if(n%2)
            {
                result += n % 2;
                n = (n-1) / 2;
            }
            else
            {
                n /=2;
            }
            result += n;
        }
        return result;
        // or return n-1;
    }
};