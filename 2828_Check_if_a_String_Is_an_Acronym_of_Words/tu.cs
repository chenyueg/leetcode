public class Solution {
    public bool IsAcronym(IList<string> words, string s) {
        if(words.Count != s.Length)
            return false;
        
        for(int i =0; i<s.Length; i++)
        {
            if(s[i] != words[i][0])
                return false;
        }
        return true;
    }
}