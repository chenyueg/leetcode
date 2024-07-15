public class Solution {
    public int ArithmeticTriplets(int[] nums, int diff) {
        int result = 0;
        HashSet<int> numsSet = new HashSet<int>(nums);
        for(int i=0; i<nums.Length; i++)
        {
            int a = nums[i];
            int b = a + diff;
            int c = b + diff;
            if(numsSet.Contains(b) && numsSet.Contains(c))
            {
                result += 1;
            }
        }
        return result;
    }
}