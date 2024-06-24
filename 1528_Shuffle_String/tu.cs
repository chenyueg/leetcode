public class Solution {
    public string RestoreString(string s, int[] indices) {
        StringBuilder sb = new StringBuilder(new string(' ', s.Length));
        for(int i=0;i<s.Length;i++)
        {
            sb[indices[i]] = s[i];
        }
        return sb.ToString();
    }
}