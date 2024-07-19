public class Solution {
    public int PivotInteger(int n) {
        int all_sum = n * (n+1) / 2;
        int sum_sqrt = (int)Math.Floor(Math.Sqrt(all_sum));
        if(sum_sqrt * sum_sqrt == all_sum)
            return sum_sqrt;
        else
            return -1;
    }
}