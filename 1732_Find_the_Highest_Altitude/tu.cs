public class Solution {
    public int LargestAltitude(int[] gain) {
        int result = 0;
        int init = 0;
        foreach(int diff in gain)
        {
            init += diff;
            result = Math.Max(result, init);
        }
        return result;
    }
}