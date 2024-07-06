public class Solution {
    public double MinimumAverage(int[] nums) {
        Array.Sort(nums);
        int result = nums[0] + nums[nums.Length - 1];
        for(int i=0; i<nums.Length; i++)
        {
            int current = nums[i] + nums[nums.Length - 1 - i];
            if(result > current)
            {
                result = current;
            }
        }
        return result / 2.0;
    }
}