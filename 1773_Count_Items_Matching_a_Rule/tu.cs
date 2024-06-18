public class Solution {
    public int CountMatches(IList<IList<string>> items, string ruleKey, string ruleValue) {
        List<string> heads = new List<string> {"type", "color", "name"};
        int index = heads.IndexOf(ruleKey);
        int result = 0;
        for(int i=0; i<items.Count; i++)
        {
            if(items[i][index] == ruleValue)
            {
                result +=1;
            }
        }
        return result;
    }
}