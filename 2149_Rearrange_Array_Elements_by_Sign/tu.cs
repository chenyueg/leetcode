public class Solution {
    public int[] RearrangeArray(int[] nums) {
        int[] result = new int[nums.Length];
        int pos = 0;
        int neg = 1;
        foreach(int num in nums)
        {
            if(num>0)
            {
                result[pos] = num;
                pos += 2;
            }
            else
            {
                result[neg] = num;
                neg += 2;
            }
        }
        return result;
    }
}