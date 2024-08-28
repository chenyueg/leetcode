public class Solution {
    public int DiagonalSum(int[][] mat) {
        int sum = 0;
        int len = mat.Length;
        for(int i=0;i<len;i++)
        {
            sum += mat[i][i];
            if(i!=len - i - 1)
                sum += mat[i][len - i - 1];
        }
        return sum;
    }
}