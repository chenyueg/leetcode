public class Solution {
    public int CountConsistentStrings(string allowed, string[] words) {
        // build allowed table
        int[] allowTable = new int[26];
        foreach(char allow in allowed)
        {
            allowTable[allow - 'a'] = 1;
        }

        int result = 0;
        foreach(string word in words)
        {   
            bool isAllowed = true;
            foreach(char c in word)
            {
                if(allowTable[c - 'a'] == 0)
                {
                    isAllowed = false;
                    break;
                }
            }
            if(isAllowed)
                result += 1;
        }
        
        return result;
    }
}