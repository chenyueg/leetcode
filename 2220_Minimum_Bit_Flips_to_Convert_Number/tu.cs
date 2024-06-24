public class Solution {
    public int MinBitFlips(int start, int goal) {
        int diff = start ^ goal;
        int result = 0;
        while(diff > 0)
        {
            if(diff%2 == 1)
            {
                result += 1;
            }
            diff = diff >> 1;
        }
        return result;
    }
}