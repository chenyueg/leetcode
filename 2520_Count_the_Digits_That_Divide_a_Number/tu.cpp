class Solution {
public:
    int countDigits(int num) {
        int temp = num;
        int result = 0;
        while(temp>0)
        {
            int current = temp % 10;
            if(num % current == 0)
            {
                result += 1;
            }
            temp /= 10;
        }
        return result;
    }
};