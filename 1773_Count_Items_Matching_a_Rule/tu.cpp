class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int index = 0;
        if(ruleKey=="color") index = 1;
        if(ruleKey=="name") index = 2;
        int result = 0;
        for(int i=0; i<items.size(); i++)
        {
            if(items[i][index] == ruleValue)
            {
                result += 1;
            }
        }
        return result;
    }
};