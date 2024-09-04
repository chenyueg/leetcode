public class Solution {
    public int SumOddLengthSubarrays(int[] arr) {
        int result = 0;
        int n = arr.Length;
        for(int i=0;i<n;i++)
        {
            result += ((i+1)*(n-i) + 1)/2 * arr[i];
        }
        return result;
    }
}