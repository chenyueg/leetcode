public class Solution {
    public string FinalString(string s) {
        bool isReverse = false;
        var sb = new StringBuilder();

        for(int i=0;i<s.Length;i++)
        {
            if(s[i] == 'i')
            {
                isReverse = !isReverse;
            }
            else
            {
                if(isReverse)
                    sb.Insert(0,s[i]);
                else
                    sb.Append(s[i]);
            }

        }

        if(isReverse)
            return new string(sb.ToString().Reverse().ToArray());
        else
            return sb.ToString();
    }
}