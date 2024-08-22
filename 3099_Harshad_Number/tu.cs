public class Solution {
    public int SumOfTheDigitsOfHarshadNumber(int x) {
        int temp = x;
        int xSum = 0;
        while(temp>0)
        {
            xSum += temp % 10;
            temp /= 10;
        }
        if(x % xSum == 0)
            return xSum;
        else
            return -1; 
    }
}