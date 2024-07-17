public class Solution {
    public IList<string> CellsInRange(string s) {
        List<string> result = new List<string>();
        int start_c = s[0] - 'A';
        int start_r = s[1] - '0';
        int end_c = s[3] - 'A';
        int end_r = s[4] - '0';

        for(int i=start_c;i<=end_c;i++)
            for(int j=start_r;j<=end_r;j++)
            {
                char c = (char)((int)('A') + i);
                char r = (char)((int)('0') + j);
                string next = new string([c, r]);
                result.Add(next);
            }
        return result;
    }
}