public class Solution {
    public int MaxCoins(int[] piles) {
        Array.Sort(piles);
        Array.Reverse(piles);
        int pick_count = piles.Length / 3;
        int result = 0;
        for(int i=0; i<pick_count; i++)
        {
            result += piles[i*2+1];
        }
        return result;
    }
}