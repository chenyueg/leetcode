public class Solution {
    public string MakeSmallestPalindrome(string s) {
        var result = s.ToCharArray();
        for(int i =0; i<s.Length/2; i++)
        {
            if(result[i] < result[s.Length - 1 - i])
                result[s.Length - 1 - i] = result[i];
            else
                result[i] = result[s.Length - 1 - i];
        }
        return new string(result);
    }
}