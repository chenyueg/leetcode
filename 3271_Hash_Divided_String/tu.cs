public class Solution {
    public string StringHash(string s, int k) {
        char[] result = new char[s.Length / k];
        int current = 0;
        for(int i=0;i<s.Length;i++)
        {
            current += s[i] - 'a';
            
            if(i % k == k-1)
            {
                result[(i+1)/k-1] = (char)('a' + (current % 26));
                current = 0;
            }
        }
        return new string(result);
    }
}