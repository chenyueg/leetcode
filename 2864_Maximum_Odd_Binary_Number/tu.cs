public class Solution {
    public string MaximumOddBinaryNumber(string s) {
        int ones = 0;
        int zeros = 0;
        for(int i=0; i<s.Length; i++)
        {
            if(s[i] == '1')
                ones += 1;
            else
                zeros += 1;
        }

        char[] newChars = new char[s.Length];
        for(int i=0; i<ones-1; i++)
            newChars[i] = '1';
        for(int i=ones-1; i<s.Length-1; i++)
            newChars[i] =  '0';
        newChars[s.Length-1] = '1';

        return new string(newChars);
    }
}