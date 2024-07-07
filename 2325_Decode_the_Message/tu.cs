public class Solution {
    public string DecodeMessage(string key, string message) {
        Dictionary<char, char> myDdict = new Dictionary<char, char>();
        int current = 0;
        string lowers = "abcdefghijklmnopqrstuvwxyz";
        for(int i=0;i<key.Length;i++)
        {
            if(char.IsLower(key[i]) && myDdict.ContainsKey(key[i])==false)
            {
                myDdict.Add(key[i], lowers[myDdict.Count]);
            }
            if(myDdict.Count==26)
                break;
        }
        char[] result_chars = new char[message.Length];
        for(int i=0;i<message.Length;i++)
        {
            if(myDdict.ContainsKey(message[i]))
                result_chars[i] = myDdict[message[i]];
            else
                result_chars[i] = message[i];
        }
        string result = new string(result_chars);
        return result;
    }
}