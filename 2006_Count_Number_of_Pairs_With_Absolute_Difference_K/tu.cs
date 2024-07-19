public class Solution {
    public int CountKDifference(int[] nums, int k) {
        Dictionary<int, int> counts = new Dictionary<int, int>();

        for(int i=0;i<nums.Length;i++)
        {
            int value = 0;
            if(counts.TryGetValue(nums[i], out value))
            {
                counts[nums[i]] += 1;
            }
            else
            {
                counts.Add(nums[i], 1);
            }
        }

        int result = 0;
        foreach(KeyValuePair<int, int> pair in counts)
        {
            int value = 0;
            if(counts.TryGetValue(pair.Key+k, out value))
            {
                result += counts[pair.Key] * counts[pair.Key+k];
            }
        }

        return result;
    }
}