public class Solution {
    public int AddedInteger(int[] nums1, int[] nums2) {
        int sum1 = nums1.Sum();
        int sum2 = nums2.Sum();
        return (sum2-sum1)/nums1.Length;
    }
}