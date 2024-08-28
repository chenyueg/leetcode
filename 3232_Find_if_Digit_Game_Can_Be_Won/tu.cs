public class Solution {
    public bool CanAliceWin(int[] nums) {
        int sumAll = nums.Sum();
        int sumSingle = 0;
        for(int i=0;i<nums.Length;i++)
        {
            if(nums[i] < 10)
                sumSingle += nums[i];
        }
        if(sumSingle * 2 == sumAll)
            return false;
        else
            return true;
    }
}