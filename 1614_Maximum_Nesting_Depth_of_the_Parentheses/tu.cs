public class Solution {
    public int MaxDepth(string s) {
        int result = 0;
        int current = 0;

        for(int i=0;i<s.Length;i++)
        {
            if(s[i] == '(')
                {
                    current += 1;
                    if(current>result)
                        result = current;
                }
            if(s[i] == ')')
                current -= 1;
        }
        return result;
    }
}