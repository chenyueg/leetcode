public class Solution {
    public string TruncateSentence(string s, int k) {
        int current = 0;
        for(int i=0; i<s.Length; i++)
        {
            if(s[i]==' ')
            {
                current += 1;
                if(current == k)
                {
                    return s.Substring(0,i);
                }
            }
        }
        return s;
    }
}