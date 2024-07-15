public class Solution {
    public int DifferenceofNumber(int num)
    {
        int result = num;
        while(num > 0)
        {
            result -= num % 10;
            num = num / 10;
        }
        return result;
    }

    public int DifferenceOfSum(int[] nums) {
        int result = 0;
        foreach(int num in nums)
        {
            result += DifferenceofNumber(num);
        }
        return result;
    }
}