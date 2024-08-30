public class Solution {
    public int CountAsterisks(string s) {
        int isOutBracket = 1;
        int result = 0;
        for(int i=0;i<s.Length;i++)
        {
            if(s[i]=='*')
            {
                result += isOutBracket;
            }
            if(s[i]=='|')
            {
                isOutBracket = 1 - isOutBracket;
            }
        }
        return result;
    }
}