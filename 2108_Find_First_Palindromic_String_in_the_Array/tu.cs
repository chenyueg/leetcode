public class Solution {
    public string FirstPalindrome(string[] words) {
        foreach(string word in words)
        {
            bool isPalindromic = true;
            for(int i=0;i<word.Length/2;i++)
            {
                if(word[i] != word[word.Length - i - 1])
                {
                    isPalindromic = false;
                    break;
                }
            }
            if(isPalindromic)
                return word;
        }

        return "";
    }
}