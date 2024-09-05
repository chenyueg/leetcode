public class Solution {
    public int MaximizeSum(int[] nums, int k) {
        int maxValue = nums.Max();
        return maxValue * k + k * (k-1) / 2;
    }
}